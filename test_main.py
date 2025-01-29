@app.post("/upload-files")
async def create_upload_files(files: List[UploadFile] = File(...)):
    resumes = []

    for file in files:
        filename = local_path + file.filename
        destination_file_path = local_path + file.filename  # output file path

        async with aiofiles.open(destination_file_path, 'wb') as out_file:
            while content := await file.read(CHUNK_SIZE):
                await out_file.write(content)  # async write file chunk

        data = resumeparse.read_file(filename)
        resumes.append(data)

    return {"Result": "OK", "resumes": resumes}