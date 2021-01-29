from fastapi import FastAPI
from fastapi import UploadFile,File
import uvicorn

app = FastAPI()

@app.get('/')
async def hello():
    return {"hello": "there"}

@app.post('/predict')
async def predict(file: UploadFile = File(...)):
    return {"all":"right"}

