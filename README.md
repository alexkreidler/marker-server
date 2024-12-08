# Marker server

Turns PDFs into nice Markdown. [Example Output](./out.md) from lecture slides

Uses pixi for fast installation

```
pixi install
TORCH_DEVICE=cpu python src/server.py

curl -v -F file=@301_MVC_Practice_Questions.pdf -X POST http://localhost:8000/convert
```

(You need to run on CPU when on Apple Silicon because it tries to use MPS but causes a segfault) Otherwise you can use cuda.

It will take a while to download the models from huggingface on first startup.