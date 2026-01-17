from networksecurity.components.data_ingestio import DataIngestion
from networksecurity.components.data_validation import DataValidation   
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

import sys

if __name__=="__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data initiation completed")
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        dataValidation=DataValidation(dataingestionconfig,data_validation_config)
        logging.info("initiate data validation")
        DataValidation.initiate_data_validation()
        print(dataingestionartifact)
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)
