from fastapi import APIRouter, UploadFile
from backend.services.file_service import handle_file_upload
from backend.services.profiling_service import profile_dataset

router = APIRouter()

@router.post("/upload")
async def upload_dataset(file: UploadFile):
    file_path = await handle_file_upload(file)
    metadata = profile_dataset(file_path)
    return {"message": "Dataset uploaded!", "metadata": metadata}