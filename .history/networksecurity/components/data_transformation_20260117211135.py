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
    
    def initiate_data_transformation(self)-> DataTransformationArtifact:
        try:
            logging.info("Data Transformation has been started")
            #reading training and testing file
            train_df=pd.read_csv(self.data_validation_artifact.valid_train_file_path)
            test_df=pd.read_csv(self.data_validation_artifact.valid_test_file_path)

            #selecting input feature for imputation
            input_feature_train_df=train_df.drop(columns=[TAGRGET_COLUMN],axis=1)
            input_feature_test_df=test_df.drop(columns=[TAGRGET_COLUMN],axis=1)

            #selecting target feature
            target_feature_train_df=train_df[TAGRGET_COLUMN]
            target_feature_test_df=test_df[TAGRGET_COLUMN]

            #imputer object
            imputer=KNNImputer(**DaTA_TRANSFORMATION_IMPUTER_PARAMS)
            



