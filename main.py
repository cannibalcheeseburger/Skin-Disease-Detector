from fastapi import FastAPI
from fastapi import UploadFile,File
import uvicorn
from random import randint
from src import const
import os

app = FastAPI()

@app.get('/')
async def hello():
    return {"hello": "there"}

@app.post('/predict')
async def predict(file: UploadFile = File(...)):
    return {"all":"right"}

@app.get('/predict/random')
async def predict_random():
    #eturn os.getcwd()
    with open(const.diagnosis_dir+ const.diseases[randint(0,11)],'r',encoding='utf-8') as f:
        diagnosis = f.read()
    return {str(randint(0,100))+'%':diagnosis}