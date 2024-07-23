import pandas as pd
import numpy as np
import joblib

from pathlib import Path
import os
import sys

# Define the root directory of the package one level up from the current file's directory
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent

# Add the package root directory to the system path to allow importing from the prediction_model package
sys.path.append(str(PACKAGE_ROOT))

from prediction_model.config import config  
from prediction_model.processing.data_handling import load_pipeline, load_dataset

# Load the pre-trained classification pipeline from the specified model file
classification_pipeline = load_pipeline(config.MODEL_NAME)

def generate_predictions(data_input):
    """
    Generate predictions using the classification pipeline.

    Parameters:
    data_input (dict or list of dicts): Input data for prediction.

    Returns:
    dict: Dictionary containing the predictions with key "prediction".
    """
    # Convert input data to a DataFrame
    data = pd.DataFrame(data_input)
    
    # Use the pipeline to predict the target variable
    pred = classification_pipeline.predict(data[config.FEATURES])
    
    # Convert prediction results to 'Y' for positive and 'N' for negative
    output = np.where(pred == 1, 'Y', 'N')
    
    # Create a dictionary with the prediction results
    result = {"prediction": output}
    return result

# Uncomment the following block to use the function with test data loading
# def generate_predictions():
#     # Load test dataset
#     test_data = load_dataset(config.TEST_FILE)
#     
#     # Use the pipeline to predict the target variable
#     pred = classification_pipeline.predict(test_data[config.FEATURES])
#     
#     # Convert prediction results to 'Y' for positive and 'N' for negative
#     output = np.where(pred == 1, 'Y', 'N')
#     print(output)
#     # Optionally, return the predictions as a dictionary
#     # result = {"Predictions": output}
#     return output

if __name__ == '__main__':
    # Example usage: generate predictions with sample data
    sample_data = [{'Feature1': 100, 'Feature2': 200}, {'Feature1': 150, 'Feature2': 250}]
    predictions = generate_predictions(sample_data)
    print(predictions)
