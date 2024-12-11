import modal
from fastapi import UploadFile
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.renderers.markdown import MarkdownOutput
import os
import shutil
import time

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

@app.function(
    image=image,
    gpu=modal.gpu.A10G(count=1),
    container_idle_timeout=20,
    timeout=24 * 60 * 60,
    allow_concurrent_inputs=1000,
)
@modal.web_endpoint(method="POST")
async def convert(file: UploadFile):
    upload_start_time = time.time()

    temp_file_path = f"/tmp/{file.filename}"
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    upload_time = time.time() - upload_start_time

    file_size = os.path.getsize(temp_file_path)

    converter = PdfConverter(
        artifact_dict=create_model_dict(),
    )

    conversion_start_time = time.time()

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