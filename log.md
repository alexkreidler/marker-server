CPU Docker

Tried ghcr.io/surnet/alpine-opencv:3.20.3-4.10.0-base, Got
```
OrbStack ERROR: Dynamic loader not found: /lib64/ld-linux-x86-64.so.2

This usually means that you're running an x86 program on an arm64 OS without multi-arch libraries.
To fix this, you can:
  1. Use an Intel (amd64) container to run this program; or
  2. Install multi-arch libraries in this container.

This can also be caused by running a glibc executable in a musl distro (e.g. Alpine), or vice versa.
```

Tried: `gcr.io/distroless/base-debian12:debug` and `hdgigante/python-opencv:4.10.0-debian`
```                                                               
WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested
Traceback (most recent call last):
  File "/app/server.py", line 52, in <module>
    app = make_server()
          ^^^^^^^^^^^^^
  File "/app/server.py", line 8, in make_server
    from marker.converters.pdf import PdfConverter
  File "/app/.pixi/envs/default/lib/python3.11/site-packages/marker/converters/pdf.py", line 8, in <module>
    from marker.builders.document import DocumentBuilder
  File "/app/.pixi/envs/default/lib/python3.11/site-packages/marker/builders/document.py", line 3, in <module>
    from marker.builders.layout import LayoutBuilder
  File "/app/.pixi/envs/default/lib/python3.11/site-packages/marker/builders/layout.py", line 4, in <module>
    from surya.layout import batch_layout_detection
  File "/app/.pixi/envs/default/lib/python3.11/site-packages/surya/layout.py", line 9, in <module>
    from surya.input.slicing import ImageSlicer
  File "/app/.pixi/envs/default/lib/python3.11/site-packages/surya/input/slicing.py", line 4, in <module>
    import cv2
  File "/app/.pixi/envs/default/lib/python3.11/site-packages/cv2/__init__.py", line 181, in <module>
    bootstrap()
  File "/app/.pixi/envs/default/lib/python3.11/site-packages/cv2/__init__.py", line 153, in bootstrap
    native_module = importlib.import_module("cv2")
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/.pixi/envs/default/lib/python3.11/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ImportError: libGL.so.1: cannot open shared object file: No such file or directory
```

For future reference: https://github.com/Dibz15/marker_docker/blob/main/Dockerfile
Has tesseract, ghostscript other stuff
10GB compressed but has models inside the image. Mine is 1.9GB but downloads on startup, or loads if you have a huggingface cache dir

TODO: investigate getting image size even smaller. Do we need torch?


Local
docker build -f ./docker/Dockerfile.cpu -t alexkreidler/marker-server:1.0.2-cpu --platform linux/amd64  --progress=plain .


```

native_module = importlib.import_module("cv2")
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/usr/local/lib/python3.11/importlib/__init__.py", line 126, in import_module
return _bootstrap._gcd_import(name[level:], package, level)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ImportError: libGL.so.1: cannot open shared object file: No such file or directory
During handling of the above exception, another exception occurred:
```

Optimized concurrent model loading, now takes about 30 seconds to load instead of over a minute. Cold start time is about 40 seconds. Cuttinng down container size

Consistently takes about 8 seconds when prewarmed. Boosting up to 4 CPUs increased execution times to around 10 seconds

Uses up to 4.3 RAM, 6.3 VRAM (on the A10Gs, less about 4.3 on the A100, maybe cause getting throttled/combined with other stuff) CPU utilization goes up to 4 cores, GPU to 20-66%

Memory doesn't really go back down?