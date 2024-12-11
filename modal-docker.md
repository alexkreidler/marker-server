Test by running `modal shell --image ghcr.io/alexkreidler/marker-server:1.0.2-modal`

this checks Modal is compatible with the image and we can get a shell.

From there we can try to run the code/app

```
=> Step 1: COPY /python/. /usr/local

=> Step 2: RUN ln -s /usr/local/bin/python3 /usr/local/bin/python

=> Step 3: ENV TERMINFO_DIRS=/etc/terminfo:/lib/terminfo:/usr/share/terminfo:/usr/lib/terminfo

=> Step 4: COPY /modal_requirements.txt /modal_requirements.txt

=> Step 6: RUN uv pip install --system --compile-bytecode --no-cache --no-deps -r /modal_requirements.txt

=> Step 7: RUN rm /modal_requirements.txt

Built image im-9fKneMCvsIkhbcMubiZM2Y in 70.05s
Building image im-9t8Ub1jZ9dq7zWTuqAeuxb

=> Step 0: FROM base
```


Runner failed with exit code: 127
python: 1: ./docker/entrypoint.sh: not found