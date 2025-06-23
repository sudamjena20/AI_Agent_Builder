from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import whisper
import uvicorn
import shutil
import os

app = FastAPI()
model = whisper.load_model("base")

@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    temp_file = f"/tmp/{file.filename}"
    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = model.transcribe(temp_file)
    os.remove(temp_file)

    return JSONResponse(content={"text": result["text"]})

if __name__ == "__main__":
    uvicorn.run("whisper_api:app", host="0.0.0.0", port=8080, reload=True)
