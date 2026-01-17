import os
import  numpy as np 
import pandas as pd 

"""defining constant variables for training pipeline"""
TAGRGET_COLUMN ="Result"
PIPELINE_NAME: str ="networksecurity"
ARTIFACT_DIR: str ="Artifact"
FILE_NAME: str ="PhishingData.csv "

TRAIN_FILE_NAME: 

""" Data ingestion related constant start with DATA_INGESTION VAR NAME """
DATA_INGESTION_COLLECTION_NAME: str="PhishingData"
DATA_INGESTION_DATABASE_NAME: str="NetworkSecurity"
DATA_INGESTION_DIR_NAME: str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str="feature_store"
DATA_INGESTION_INGESTED_DIR: str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float=0.2



