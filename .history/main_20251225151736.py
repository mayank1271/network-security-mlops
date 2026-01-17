from networksecurity.components.data_ingestio import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig

if __name__=="__main__":
    try:
        dataingestionconfig=DataIngestionConfig()
        data_ingestion=DataIngestion(dataingestionconfig)
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        raise NetworkSecurityException(e,sys)
