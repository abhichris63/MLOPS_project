import os
from src.exception import CustomException
from src.logger import get_logger
import yaml
import sys
import pandas as pd

logger = get_logger(__name__)

# Operations for YAML file

# Read yaml file
def read_yaml(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError("File is not present in the path")
        
        with open(file_path, "r") as read_yaml_file:
            config = yaml.safe_load(read_yaml_file)
            logger.info("Successfully YAML file reading operation is done...")
            return config
    except Exception as e:
        logger.error("Error while reading YAML file..")
        raise CustomException("Failed to Read the file",e)
    
# Loading Data
def load_data(path):
    try:
        df = pd.read_csv(path)
        logger.info(f"Data Loaded Successfully from path: {path}")
        return df
    except Exception as e:
        logger.error("Error while Loading the Data")
        raise CustomException("Failed to Load the Data",e)