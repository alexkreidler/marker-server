
from beam import Image, asgi, endpoint
from beam import CloudBucket, CloudBucketConfig, function

image = (
    Image(
        base_image="nvidia/cuda:12.3.2-runtime-ubuntu22.04",
        python_version="python3.11",
    )
    .add_commands(["apt-get update -y", "apt-get install libglapi-mesa libegl-mesa0 libegl1 libopengl0 libgl1-mesa-glx libglib2.0-0 libsm6 libxrender1 libxext6 -y"])
    .add_python_packages(["fastapi", "torch", "scipy", "numpy", "marker-pdf", "python-multipart"])
)


def init_models():
    from marker.converters.pdf import PdfConverter
    from marker.models import create_model_dict
    converter = PdfConverter(
        artifact_dict=create_model_dict("cuda"),
    )
    return converter

research_docs = CloudBucket(
    name="research_docs",
    mount_path="./research_docs",
    config=CloudBucketConfig(
        access_key="S3_KEY",
        secret_key="S3_SECRET",
        read_only=True,
    ),
)


# WIP
@endpoint(
    name="marker-pdf-converter-4",
    image=image,
    on_start=init_models,
    memory=2048,
    volumes=[research_docs]
)
def handler(context, **args):
    import time
    start_time = time.time()
    from marker.converters.pdf import PdfConverter
    from marker.models import create_model_dict
    from marker.renderers.markdown import MarkdownOutput
    import os

    converter = context.on_start_value

    file_name = args["file_name"]
    if not file_name:
        return "Error: no file name provided"
    
    file_path = os.path.join(research_docs.mount_path, file_name)
    
    conversion_start_time = time.time()

    rendered: MarkdownOutput = converter(file_path)

    conversion_time = time.time() - conversion_start_time

    return {
        "filename": file_name,
        "size": os.path.getsize(file_path),
        "start_time": start_time,
        "conversion_duration": conversion_time,
        "markdown": rendered.markdown
    }