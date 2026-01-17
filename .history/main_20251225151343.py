from networksecurity.components.data_ingestio import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
rom networksecurity.logging import logger
from networksecurity.logging.logger import logging

if __name__=="__main__":
    try:
        logger.logging.info("Enter the try block")
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        raise NetworkSecurityException(e,sys)
