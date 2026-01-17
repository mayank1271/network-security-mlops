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
        
    @staticmethod
    def read_data(file_path)->pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            train_file_path=self.data_ingestion_artifact.train_file_path
            test_file_path=self.data_ingestion_artifact.test_file_path

        ## read the data from train and test
        train_dataframe=Data

            #create valid and invalid dir
            os.makedirs(self.data_validation_congfig.valid_data_dir,exist_ok=True)
            os.makedirs(self.data_validation_congfig.invalid_data_dir,exist_ok=True)

            #valid file path
            valid_train_file_path=os.path.join(
                self.data_validation_congfig.valid_data_dir,
                os.path.basename(train_file_path)
            )

            valid_test_file_path=os.path.join(
                self.data_validation_congfig.valid_data_dir,
                os.path.basename(test_file_path)
            )

            #invalid file path
            invalid_train_file_path=os.path.join(
                self.data_validation_congfig.invalid_data_dir,
                os.path.basename(train_file_path)
            )

            invalid_test_file_path=os.path.join(
                self.data_validation_congfig.invalid_data_dir,
                os.path.basename(test_file_path)
            )

            #let's do the ks test for drift detection
            status=True

            for column in train_dataframe.columns:
                d1=train_dataframe[column]
                d2=test_dataframe[column]

                ks_test_statistic,p_value=ks_2samp(d1,d2)

                if p_value<0.05:
                    status=False
                    train_dataframe.to_csv(invalid_train_file_path,index=False)
                    test_dataframe.to_csv(invalid_test_file_path,index=False)
                    break
            
            if status:
                train_dataframe.to_csv(valid_train_file_path,index=False)
                test_dataframe.to_csv(valid_test_file_path,index=False)

            data_validation_artifact=DataValidationArtifact(
                validation_status=status,
                valid_train_file_path=valid_train_file_path,
                valid_test_file_path=valid_test_file_path,
                invalid_train_file_path=invalid_train_file_path,
                invalid_test_file_path=invalid_test_file_path,
                drift_report_file_path=""
            )

            logging.info(f"Data Validation artifact:{data_validation_artifact}")
            return data_validation_artifact

        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    

