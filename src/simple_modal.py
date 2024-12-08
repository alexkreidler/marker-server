import modal
from server import make_server
app = modal.App("marker")

@app.function(
    image=modal.Image.from_registry("alexkreidler/marker-server:1.0.2-modal"),
    gpu=modal.gpu.A10G(count=1),
    container_idle_timeout=20,
    timeout=24 * 60 * 60,
    allow_concurrent_inputs=1000,
)
@modal.asgi_app()
def serve():
    return make_server()