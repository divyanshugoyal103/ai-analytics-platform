import os
from fastapi import UploadFile
import shutil

UPLOAD_DIR = "./datasets/"

async def handle_file_upload(file: UploadFile):
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    upload_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(upload_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return upload_path