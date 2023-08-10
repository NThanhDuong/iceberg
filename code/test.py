from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TableInfo(BaseModel):
    name: str
    schema: str
    location: str

# Đây là dữ liệu mẫu, bạn cần thay thế thông tin tương ứng từ MinIO
table_info_data = {
    "name": "person",
    "schema": "name:string,age:int,address:string",
    "location": "s3://warehouse/person"
}

@app.get("/get_table_info")
async def get_table_info():
    return TableInfo(**table_info_data)
