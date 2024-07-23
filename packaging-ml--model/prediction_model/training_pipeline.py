import pandas as pd
import numpy as np 
from pathlib import Path
import os
import sys

# Add the package root directory to the system path to avoid module not found error
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

# Import necessary modules from the prediction_model package
from prediction_model.config import config  
from prediction_model.processing.data_handling import load_dataset, save_pipeline
import prediction_model.processing.preprocessing as pp 
import prediction_model.pipeline as pipe 

def perform_training():
    """
    Load training data, train the classification pipeline, and save the trained model.
    """
    # Load the training dataset
    train_data = load_dataset(config.TRAIN_FILE)
    
    # Map the target variable 'Loan_Status' to binary values: 'N' to 0, 'Y' to 1
    train_y = train_data[config.TARGET].map({'N': 0, 'Y': 1})
    
    # Train the classification pipeline using the specified features and target variable
    pipe.classification_pipeline.fit(train_data[config.FEATURES], train_y)
    
    # Save the trained classification pipeline
    save_pipeline(pipe.classification_pipeline)

if __name__ == '__main__':
    # Perform training when the script is run directly
    perform_training()
