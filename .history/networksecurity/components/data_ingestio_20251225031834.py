from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


## configuration of the data ingestion config

from networksecurity.entity.config_entity import DataIngestionConfig    

import os
import sys  
import pymango
from typing import list
 from sklearn.model_selection import train_test_split