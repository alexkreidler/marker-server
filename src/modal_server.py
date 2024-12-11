from typing import Callable
import modal
from fastapi import UploadFile
from marker.converters.pdf import PdfConverter
from marker.renderers.markdown import MarkdownOutput
import os
import shutil
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from marker import models
from transformers import PreTrainedModel

def load_models_concurrently(load_functions_map: dict[str, Callable]) -> dict[str, PreTrainedModel]:
    model_id_to_model = {}
    with ThreadPoolExecutor(max_workers=len(load_functions_map)) as executor:
        future_to_model_id = {
            executor.submit(load_fn): model_id
            for model_id, load_fn in load_functions_map.items()
        }
        for future in as_completed(future_to_model_id.keys()):
            model_id_to_model[future_to_model_id[future]] = future.result()
    return model_id_to_model

def create_model_dict_concurrent(device=None, dtype=None):
    load_functions_map = {
        "layout_model": lambda: models.setup_layout_model(device, dtype),
        "texify_model": lambda: models.setup_texify_model(device, dtype),
        "recognition_model": lambda: models.setup_recognition_model(device, dtype),
        "table_rec_model": lambda: models.setup_table_rec_model(device, dtype),
        "detection_model": lambda: models.setup_detection_model(device, dtype),
    }
    return load_models_concurrently(load_functions_map)

app = modal.App("marker")

image = (
    modal.Image.from_registry("ghcr.io/alexkreidler/marker-server:1.0.2-modal-2", add_python="3.10")
    .pip_install("fastapi", "torch", "scipy", "numpy", "marker-pdf", "python-multipart")
    .copy_local_file("./modal-entrypoint.sh", "/modal-entrypoint.sh")
    .dockerfile_commands([
                "RUN chmod +x /modal-entrypoint.sh",
            ]
        )
        .entrypoint(["/modal-entrypoint.sh"])

)


@app.cls(
    image=image,
    gpu=modal.gpu.A10G(count=1),
    cpu=(1, 6),
    memory=(2048, 6144),
    container_idle_timeout=20,
    timeout=24 * 60 * 60,
    allow_concurrent_inputs=1000,
)
class ConverterModel:
    # https://modal.com/docs/guide/lifecycle-functions#lifecycle-hooks-for-web-endpoints
    @modal.enter()
    def setup_models(self):
        print("Loading models concurrently")
        self.artifact_dict = create_model_dict_concurrent()
        self.converter = PdfConverter(self.artifact_dict)
        print("Created converter class")

    def convert_file(self, file_path: str) -> MarkdownOutput:
        print(f"Running conversion on file {file_path}")
        converter = PdfConverter(artifact_dict=self.artifact_dict)
        return converter(file_path)
        
    @modal.web_endpoint(method="POST")
    async def convert(self, file: UploadFile):
        upload_start_time = time.time()

        temp_file_path = f"/tmp/{file.filename}"
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        upload_time = time.time() - upload_start_time

        file_size = os.path.getsize(temp_file_path)

        conversion_start_time = time.time()
        converter = self.converter

        rendered: MarkdownOutput = converter(temp_file_path)

        os.remove(temp_file_path)

        conversion_time = time.time() - conversion_start_time

        return {
            "filename": file.filename,
            "size": file_size,
            "upload_time": upload_time,
            "conversion_time": conversion_time,
            "markdown": rendered.markdown
        }

