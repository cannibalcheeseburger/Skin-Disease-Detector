from fastapi import FastAPI
from fastapi import UploadFile,File
import uvicorn

app = FastAPI()

@app.post('/predict')
async def predict(file: UploadFile = File(...)):
    return 'ok'
