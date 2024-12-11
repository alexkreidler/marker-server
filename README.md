# Marker server

Turns PDFs into nice Markdown. [Example Output](./data/out.md) from a paper.

Uses pixi for fast installation

```
pixi install
TORCH_DEVICE=cpu python src/server.py

curl -v -F file=@301_MVC_Practice_Questions.pdf -X POST http://localhost:8000/convert
```

(You need to run on CPU when on Apple Silicon because it tries to use MPS but causes a segfault) Otherwise you can use cuda.

It will take a while to download the models from huggingface on first startup.


## Run with Docker

```
docker run -it -p 8000:8000 -v ~/.cache/huggingface/hub:/root/.cache/huggingface/hub alexkreidler/marker-server:1.0.2-cpu
```

This uses your local huggingface cache dir

Note: make sure you are running the right image for your CPU architecture.

Also, this doesn't run great on CPUs, it takes about 40 seconds to process a small document on my M3 Macbook Air

Still a few bugs with multi-col layout