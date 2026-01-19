import os,sys
import certifi
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
from starlette.responses import redirectResponse
import pandas as pd

from networksecurity.utils.main_utils.utils import load_object

client=pymongo.MongoClient(mangodb_uri,tlsCAFile=ca)

from networksecurity.constant.training_pipeline import DATA_INGESTION_COLLECTION_NAME
from networksecurity.constant.training_pipeline import DATA_INGESTION_DATABASE_NAME

database=client[DATA_INGESTION_DATABASE_NAME]
collection=database[DATA_INGESTION_COLLECTION_NAME]

app =FastAPI()
origin




