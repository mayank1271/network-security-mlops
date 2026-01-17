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
    
    def _initiate_data_transformation(self)->Pipeline:
        try:
            imputer_params=DaTA_TRANSFORMATION_IMPUTER_PARAMS
            knn_imputer=KNNImputer(
                n_neighbors=imputer_params['n_neighbors'],
                weights=imputer_params['weights'],
                missing_values=np.nan
            )
            logging.info("KNN Imputer has been initiated")
            return Pipeline(steps=[
                ('KNNImputer',knn_imputer)
            ])
        except Exception as e:
            raise NetworkSecurityException(e,sys) from e


