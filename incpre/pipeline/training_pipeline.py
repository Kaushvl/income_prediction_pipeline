import os, sys
from incpre.logger import logging
from incpre.exception import CustmeException
from incpre.components.data_ingestion import DataIngestion
from incpre.components.data_transformation import DataTransformation
from incpre.components.model_trainer import ModelTrainer
from dataclasses import dataclass



if __name__ == '__main__':
    obj = DataIngestion()
    train_data_path , test_data_path = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr , test_arr, _ = data_transformation.initiate_data_transformation(train_data_path,test_data_path)

    model_trainer = ModelTrainer()
    model_trainer.initiate_model_trainer(train_arr, test_arr)