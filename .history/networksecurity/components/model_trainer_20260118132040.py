import os,sys
from networksecurity.entity.artifact_entity import DataTransformationArtifact
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
            logging.info("Loading transformed training and testing array")
            train_array = load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_train_file_path)
            test_array = load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_test_file_path)

            logging.info("Splitting input and target feature from training and testing array")
            x_train, y_train = train_array[:, :-1], train_array[:, -1]
            x_test, y_test = test_array[:, :-1], test_array[:, -1]

            # Here you can define and train your model. For demonstration, let's assume a simple model.
            from sklearn.ensemble import RandomForestClassifier
            model = RandomForestClassifier()
            model.fit(x_train, y_train)

            logging.info("Predicting on training and testing data")
            y_train_pred = model.predict(x_train)
            y_test_pred = model.predict(x_test)

            logging.info("Calculating classification scores")
            train_metric = get_classification_score(y_true=y_train, y_pred=y_train_pred)
            test_metric = get_classification_score(y_true=y_test, y_pred=y_test_pred)

            logging.info(f"Train Metric: {train_metric}")
            logging.info(f"Test Metric: {test_metric}")

            # Save the trained model
            network_model = NetworkModel(preprocessor=None, model=model)  # Assuming preprocessor is None for simplicity
            save_object(file_path=self.model_trainer_config.trained_model_file_path, obj=network_model)

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path=self.model_trainer_config.trained_model_file_path,
                train_metric=train_metric,
                test_metric=test_metric
            )

            logging.info("Model training completed successfully")
            return model_trainer_artifact

        except Exception as e:
            raise NetworkSecurityException(e, sys) from e