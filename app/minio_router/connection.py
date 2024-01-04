from minio import Minio
from io import BytesIO
from fastapi import APIRouter, File, UploadFile
minio_router = APIRouter()
minioClient = Minio('localhost:9000',
                    access_key='Q3AM3UQ867SPQQA43P2',
                    secret_key='TEST',
                    secure=False) # TODO not product

@minio_router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_content = await file.read()
    file_size = len(file_content)
    bucket_name = 'test'
    object_name = file.filename

    minioClient.put_object(bucket_name, object_name, BytesIO(file_content), file_size)

    return {"filename": file.filename}

@minio_router.get("/check/")
async def check():
    return minioClient.bucket_exists("test")