import os
import pandas as pd
import joblib
from prediction_model.config import config

def load_dataset(file_name):
    filepath=os.path.join(config.Datapath,file_name)
    _data=pd.read_csv(filepath)
    return _data

def save_pipeline(pipeline_to_save):
    save_path=os.path.join(config.SAVED_MODEL,config.Model_name)
    joblib.dump(pipeline_to_save,save_path)
    print(f"Model Has been saved under the name {config.Model_name}")

def load_pipeline(pipeline_to_load):
    save_path=os.path.join(config.SAVED_MODEL,config.Model_name)
    model_loaded=joblib.load(save_path)
    print(f"Model Has been loaded ")
    return model_loaded