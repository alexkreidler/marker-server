
from beam import Image, asgi, endpoint
from beam import CloudBucket, CloudBucketConfig, function

image = (
    Image(
        base_image="ghcr.io/alexkreidler/marker-server:1.0.2-beam"
    )
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
    name="research-documents",
    mount_path="./research_docs",
    config=CloudBucketConfig(
        access_key="S3_KEY",
        secret_key="S3_SECRET",
        endpoint="https://s3.us-east-005.backblazeb2.com",
        read_only=True,
    ),
)


# WIP
@endpoint(
    name="marker-pdf-converter-5",
    image=image,
    on_start=init_models,
    memory=2048,
    gpu="T4",
    volumes=[research_docs]
)
def handler(context, **args):
    import time
    start_time = time.time()
    from marker.renderers.markdown import MarkdownOutput
    import os

    converter = context.on_start_value

    file_name = args["file_name"]
    if not file_name:
        return "Error: no file name provided"
    
    print(f"Starting to convert {file_name}")
    
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