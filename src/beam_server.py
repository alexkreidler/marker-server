from beam import Image, asgi

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

@asgi(
    name="marker-pdf-converter-3",
    image=image,
    on_start=init_models,
    memory=2048,
)
def handler(context):
    from server import make_server

    converter = context.on_start_value

    app = make_server(converter)

    return app