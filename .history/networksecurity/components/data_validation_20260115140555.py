from networksecurity.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.constant.training_pipeline import SCHEMA_FILE_PATH
from scipy.stats import ks_2samp
import pandas as pd
import os,sys
from networksecurity.utils.main_utils.utils import read_yaml_file

class DataValidation:
    def __init__(self,data_ingestion_artifact:DataIngestionArtifact,
                 data_validation_congfig:DataValidationConfig):
        
        try:
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_validation_congfig=data_validation_congfig
            self.schema_config=read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def initiate_data_validation(self) -> DataValidationArtifact:
        
        try:
            logging.info("Starting data validation")
            #reading the training and testing file
            train_file_path=self.data_ingestion_artifact.train_file_path
            test_file_path=self.data_ingestion_artifact.test_file_path
            train_dataframe=pd.read_csv(train_file_path)
            test_dataframe=pd.read_csv(test_file_path)

            #validating the training file
            logging.info("Validating training file")
            valid_train_file_path,invalid_train_file_path=self.validate_dataset(train_dataframe,
                                                                               self.data_validation_congfig.valid_train_file_path,
                                                                               self.data_validation_congfig.invalid_data_dir,
                                                                               "train")

            #validating the testing file
            logging.info("Validating testing file")
            valid_test_file_path,invalid_test_file_path=self.validate_dataset(test_dataframe,
                                                                             self.data_validation_congfig.valid_data_dir,
                                                                             self.data_validation_congfig.invalid_data_dir,
                                                                             "test")
            
            #returning the data validation artifact
            data_validation_artifact=DataValidationArtifact(
                validation_status=True,
                valid_train_file_path=valid_train_file_path,
                valid_test_file_path=valid_test_file_path,
                invalid_train_file_path=invalid_train_file_path,
                invalid_test_file_path=invalid_test_file_path,
                drift_report_file_path=""
            )
            logging.info(f"Data validation artifact:{data_validation_artifact}")
            return data_validation_artifact

        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    

