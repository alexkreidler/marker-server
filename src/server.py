from typing import Any


def make_server(converter: Any = None):
    import time
    from fastapi import FastAPI, File, UploadFile
    from fastapi.responses import JSONResponse
    from marker.converters.pdf import PdfConverter
    from marker.models import create_model_dict
    from marker.renderers.markdown import MarkdownOutput
    import os
    import shutil

    app = FastAPI()

    converter = converter if converter else PdfConverter(
        artifact_dict=create_model_dict(),
    )

    @app.post("/convert")
    async def convert_pdf(file: UploadFile = File(...)):
        upload_start_time = time.time()

        temp_file_path = f"/tmp/{file.filename}"
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        upload_time = time.time() - upload_start_time

        file_size = os.path.getsize(temp_file_path)

        conversion_start_time = time.time()

        rendered: MarkdownOutput = converter(temp_file_path)

        os.remove(temp_file_path)

        conversion_time = time.time() - conversion_start_time

        return JSONResponse(content={
            "filename": file.filename,
            "size": file_size,
            "upload_time": upload_time,
            "conversion_time": conversion_time,
            "markdown": rendered.markdown
        })
    
    return app

if __name__ == "__main__":
    import uvicorn
    app = make_server()
    uvicorn.run(app, host="0.0.0.0", port=8000)