from beam import Image, asgi

def init_models():
    from marker.converters.pdf import PdfConverter
    from marker.models import create_model_dict
    converter = PdfConverter(
        artifact_dict=create_model_dict(),
    )
    return converter

@asgi(
    name="marker-pdf-converter",
    image=Image(base_image="ghcr.io/alexkreidler/marker-server:1.0.2-beam"),
    on_start=init_models,
    memory=2048,
    
)
def handler(context):
    from server import make_server

    converter = context.on_start_value

    app = make_server(converter)

    return app