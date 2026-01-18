from networksecurity.constant.training_pipeline import SAVED_MODEL_DIR,MODEL_FILE_NAME

import os,sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class networksecurityModelEstimator:
    def __init__(self,model):
        try:
            self.model=model
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def predict(self,X):
        try:
            logging.info("Entered the predict method of networksecurityModelEstimator class")
            y_pred=self.model.predict(X)
            logging.info("Exited the predict method of networksecurityModelEstimator class")
            return y_pred
        except Exception as e:
            raise NetworkSecurityException(e,sys) from e
