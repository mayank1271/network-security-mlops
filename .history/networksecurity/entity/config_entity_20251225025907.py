from datetime import datetime
import os
from networksecurity.constant import training_pipeline

print(training_pipeline.PIPELINE_NAME)
print(training_pipeline.ARTIFACT_DIR)

class TrainingPipelineConfig:
    def __init__(self,timestamp=datetime.now()):
        timestamp=timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.PIPELINE_NAME=training_pipeline.PIPELINE_NAME
        self.arti=training_pipeline.ARTIFACT_DIR
        self.TIMESTAMP=timestamp

class DataIngestionConfig:
    def __init__(self,training_pipeline_config):

