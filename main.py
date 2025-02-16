from typing import Union
from fastapi import FastAPI, File, UploadFile
import aiofiles
from typing import List
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from resume_parser import resumeparse
import logging

logger = logging.getLogger(__name__)

app = FastAPI()
# dir_path = r'/home/admin/projectDir/staffingapp/media/'
# local_path = "/home/admin/projectDir/mlapi/resumes_v2/"
local_path = "resumes_v12/"

"""origins = [
    "http://localhost",
    "http://localhost:4200",
    "https://staff.opallius.com"
]
"""

# origins = ["*"]
origins = [
    "https://staff.opallius.com",
    "https://staff.opallius.com/",
    "https://opallius.com/",
    "http://localhost:4200",
    "https://staging.opallius.com",
    "http://164.68.100.175:4200",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Candidate(BaseModel):
    id: str
    resume: float


@app.get("/")
def read_root():
    data = resumeparse.read_file('NareshResume.pdf')
    return data


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/resume_parser/")
async def post(item: Candidate):
    path = dir_path + item.resume
    data = resumeparse.read_file(path)
    return data


@app.post("/upload-file")
async def create_upload_file(files: UploadFile = File(...)):
    destination_file_path = local_path + files.filename  # location to store file
    async with aiofiles.open(destination_file_path, 'wb') as out_file:
        while True:
            content = await files.read(1024)  # async read file chunk
            if not content:
                break
            await out_file.write(content)  # async write file chunk

    return {"Result": "OK", "filenames": files.filename}


# # 611451271

@app.post("/upload-files")
async def create_upload_files(files: List[UploadFile] = File(...)):
    resumes = []
    for file in files:
        logger.info(file.filename)
        filename = local_path + file.filename
        destination_file_path = local_path + file.filename  # output file path
        async with aiofiles.open(destination_file_path, 'wb') as out_file:
            while True:
                content = await file.read(1024)  # async read file chunk
                if not content:
                    break
                await out_file.write(content)  # async write file chunk

    #resumes = []
    #for file in files:
       # filename = local_path + file.filename
        data = resumeparse.read_file(filename)
        resumes.append(data)
    return {"Result": "OK", "resumes": resumes}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Candidate):
    return {"item_name": item.id, "item_id": item_id}
