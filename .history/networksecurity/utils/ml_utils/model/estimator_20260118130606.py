from networksecurity.constant.training_pipeline import SAVED_MODEL_DIR,MODEL_FILE_NAME

import os,sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkModel:
    def __innit__(self,preprocessor,model):
        try:
            self.preprocessor=preprocessor
            self.model=model
        except Exception as e:
            raise NetworkSecurityException(e,sys) 
    
    def predict(self,X):
        try:
            logging.info("Entered the predict method of NetworkModel class")
            transformed_feature=self.preprocessor.transform(X)
            logging.info("Used preprocessor to transform the data")
            y_pred
        
