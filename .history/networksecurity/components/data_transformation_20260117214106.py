import os,sys
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline
from networksecurity.constant.training_pipeline import TAGRGET_COLUMN
from networksecurity.constant.training_pipeline import DaTA_TRANSFORMATION_IMPUTER_PARAMS

from networksecurity.entity.artifact_entity import DataIngestionArtifact, DataTransformationArtifact, DataValidationArtifact
from networksecurity.entity.config_entity import DataTransformationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.utils.main_utils.utils import save_numpy_array_data, save_object

class DataTransformation:
    def __init__(self, data_validation_artifact:DataValidationArtifact,
                 data_transformation_config:DataTransformationConfig):
        try:
            self.data_validation_artifact:DataValidationArtifact=data_validation_artifact
            self.data_transformation_config:DataTransformationConfig=data_transformation_config
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    @staticmethod
    def read_data(file_path)->pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def get_data_transformation_object(self)->Pipeline:
        """
        Docstring for get_data_transformation_object

        :param self: Description
        :return: Description
        :rtype: Pipeline
        """
        logging.info("entered the get_data_transformation_object method of DataTransformation class")
        try:
            imputer:KNNImputer=KNNImputer(**DaTA_TRANSFORMATION_IMPUTER_PARAMS)
            logging.info(
                f"initialized KNNimputer with{DaTA_TRANSFORMATION_IMPUTER_PARAMS}"
            )
            processor:Pipeline=Pipeline([("imputer",imputer)])

            return processor

        except Exception as e:
            raise NetworkSecurityException(e,sys) from e
    
    def _initiate_data_transformation(self)->Pipeline:
        logging.info("Entered the _initiate_data_transformation method of DataTransformation class")
        try:
            logging.info("starting data transformation")
            train_df=self.read_data(self.data_validation_artifact.valid_train_file_path)
            test_df=self.read_data(self.data_validation_artifact.valid_test_file_path)

            ## training dataframe
            input_feature_train_df=train_df.drop(columns=[TAGRGET_COLUMN],axis=1)
            target_feature_train_df=train_df[TAGRGET_COLUMN]
            target_feature_train_df=target_feature_train_df.replace(-1,0)

            ## testing dataframe
            input_feature_test_df=test_df.drop(columns=[TAGRGET_COLUMN],axis=1)
            target_feature_test_df=test_df[TAGRGET_COLUMN]
            target_feature_test_df=target_feature_test_df.replace(-1,0)

            preprocessor=self.get_data_transformation_object()

            preprocessor_object=preprocessor.fit(input_feature_train_df)
            transformed_input_train_features=preprocessor_object.transform(input_feature_train_df)
            transformed_input_test_features=preprocessor_object.transform(input_feature_test_df)

            train_arr=np.c_[transformed_input_train_features,np.array(target_feature_train_df)]
            test_arr=np.c_[transformed_input_test_features,np.array(target_feature_test_df)]

            ### save numpy array
            save_numpy_array_data(
                file_path=self.data_transformation_config.transformed_train_file_path,
                array=train_arr, 
            )   
            save_numpy_array_data(
                file_path=self.data_transformation_config.transformed_test_file_path,
                array=test_arr,
            )       
            ## save object
            save_object( self.data_transformation_config.transformed_object_file_path,
                preprocessor_object,
            )
    


            
            
        except Exception as e:
            raise NetworkSecurityException(e,sys) from e


