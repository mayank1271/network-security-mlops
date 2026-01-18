import os,sys
from networksecurity.entity.artifact_entity import DataTransformationArtifact, ModelTrainerArtifact
from networksecurity.entity.config_entity import ModelTrainerConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.utils.ml_utils.model.estimator import NetworkModel
from networksecurity.utils.ml_utils.metric.classification_metric import get_classification_score   


from networksecurity.utils.main_utils.utils import save_object,load_object
from networksecurity.utils.main_utils.utils import load_numpy_array_data

class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig, data_transformation_artifact: DataTransformationArtifact):
        try:
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
        
    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        try:
          
            train_array = load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_train_file_path)
            test_array = load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_test_file_path)

            logging.info("Splitting input and target feature from training and testing array")
            x_train, y_train = train_array[:, :-1], train_array[:, -1]
            x_test, y_test = test_array[:, :-1], test_array[:, -1]

            # Here you can define and train your model. For demonstration, let's assume a simple model.
            from sklearn.ensemble import RandomForestClassifier
            model = RandomForestClassifier()
            mod

        except Exception as e:
            raise NetworkSecurityException(e, sys) from e