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

from 


