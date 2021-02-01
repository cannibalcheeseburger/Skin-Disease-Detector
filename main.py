from fastapi import FastAPI, Request,UploadFile,File
from fastapi.templating import Jinja2Templates
import uvicorn
from random import randint
from src import const,preprocess
import os
import shutil

templates =  Jinja2Templates(directory="./Frontend/templates")

app = FastAPI()

@app.get('/')
async def home(request : Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.post('/predict')
async def predict(image: UploadFile = File(...)):
    save_to_disk(image,path="temp",save_as='temp')
    result =  preprocess.predict()
    with open(const.diagnosis_dir + const.diseases[result],'r',encoding='utf-8') as f:
        diagnosis = f.read()
    return {const.diseases[result]: diagnosis}

def save_to_disk(uploadedfile,path='.',save_as='default'):
        extension = os.path.splitext(uploadedfile.filename)[-1]
        temp_file = os.path.join(path,save_as+extension)
        with open(temp_file,'wb') as buffer:
            shutil.copyfileobj(uploadedfile.file,buffer)