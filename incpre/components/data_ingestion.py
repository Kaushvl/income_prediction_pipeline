from src.logger import logging 
import pandas as pd
import numpy as np
import os,sys
from incpre.exception import CustmeException
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from incpre.components.data_transformation import DataTransformation
from incpre.components.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join("artifact/data_ingestion","train.csv")
    test_data_path = os.path.join("artifact/data_ingestion","test.csv")
    raw_data_path = os.path.join("artifact/data_ingestion","raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            logging.info("Data reading from local directory")
            data = pd.read_csv("data\income_cleandata.csv")
            logging.info("data reading completed")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)\

            logging.info("data splitted into train and test")
            train_set , test_set = train_test_split(data, test_size=.3,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index = False)
            test_set.to_csv(self.ingestion_config.test_data_path, index = False)

            logging.info("data ingestion completed")
            return (self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path)


        except Exception as e:
            raise CustmeException(e, sys)
        


if __name__ == "__main__":
    obj = DataIngestion()
    train_path, test_path = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr, test_arr , _ = data_transformation.initiate_data_transformation(train_path, test_path)

    model_trainer = ModelTrainer()
    model_trainer.initiate_model_trainer(train_arr,test_arr)