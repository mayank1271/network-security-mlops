import os,sys
import certifi

from networksecurity.utils.ml_utils.model.estimator import NetworkModel
ca=certifi.where()

from dotenv import load_dotenv
load_dotenv()
mangodb_uri=os.getenv("MONGODB_URI")
print(mangodb_uri)
import pymongo
from networksecurity.logging.logger import logging  
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.pipeline.training_pipeline import TrainingPipeline

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI,File,UploadFile,Request
from uvicorn import run as app_run
from fastapi.responses import Response
from starlette.responses import RedirectResponse
import pandas as pd

from networksecurity.utils.main_utils.utils import load_object

client=pymongo.MongoClient(mangodb_uri,tlsCAFile=ca)

from networksecurity.constant.training_pipeline import DATA_INGESTION_COLLECTION_NAME
from networksecurity.constant.training_pipeline import DATA_INGESTION_DATABASE_NAME

database=client[DATA_INGESTION_DATABASE_NAME]
collection=database[DATA_INGESTION_COLLECTION_NAME]

app =FastAPI()
origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],    
    allow_headers=["*"],
)

from fastapi.templating import Jinja2Templates
templates=Jinja2Templates(directory="./templates")

@app.get("/",tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train_route():
    try:
        training_pipeline=TrainingPipeline()
        training_pipeline.run_pipeline()
        return Response(content="Training successfull!!")
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
@app.post("/predict")
async def predict_route(request:Request,file:UploadFile=File(...)):
    try:
        df=pd.read_csv(file.file)
        #print(df)
        preprocesor=load_object("final_model/preprocessor.pkl")
        final_model=load_object("final_model/NetworkModel.pkl")
        network_model=NetworkModel(preprocessor=preprocesor,model=final_model)
        print(df.iloc[0])
        y_pred=network_model.predict(df)
        print(y_pred)
        df["prediction_column"]=y_pred
        print(df["prediction_column"])
        #df["prediction_column"].replace(-1,0)
        #return df.to_json()
        
        
        return templates.TemplateResponse("prediction.html",{"request":request,"results":results})
    except Exception as e:
        raise NetworkSecurityException(e,sys)

    
if __name__=="__main__":
    app_run(app,host="localhost",port=8000)




