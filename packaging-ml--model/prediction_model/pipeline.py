from sklearn.pipeline import Pipeline
from pathlib import Path
import os
import sys

# Define the root directory of the package one level up from the current file's directory
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent

# Add the package root directory to the system path to allow importing from the prediction_model package
sys.path.append(str(PACKAGE_ROOT))

from prediction_model.config import config
import prediction_model.processing.preprocessing as pp 
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
import numpy as np

# Define the classification pipeline with a series of preprocessing steps and a final classifier
classification_pipeline = Pipeline(
    [
        # Custom transformer for domain-specific processing: modifying a variable by adding another variable
        ('DomainProcessing', pp.DomainProcessing(variable_to_modify=config.FEATURE_TO_MODIFY,
                                                  variable_to_add=config.FEATURE_TO_ADD)),
        
        # Custom transformer for imputing missing values in numerical features with the mean of the column
        ('MeanImputation', pp.MeanImputer(variables=config.NUM_FEATURES)),
        
        # Custom transformer for imputing missing values in categorical features with the mode of the column
        ('ModeImputation', pp.ModeImputer(variables=config.CAT_FEATURES)),
        
        # Custom transformer for dropping specified columns
        ('DropFeatures', pp.DropColumns(variables_to_drop=config.DROP_FEATURES)),
        
        # Custom transformer for label encoding categorical features
        ('LabelEncoder', pp.CustomLabelEncoder(variables=config.FEATURES_TO_ENCODE)),
        
        # Custom transformer for applying logarithmic transformation to numerical features
        ('LogTransform', pp.LogTransforms(variables=config.LOG_FEATURES)),
        
        # Scaler for normalizing features to a range between 0 and 1
        ('MinMaxScale', MinMaxScaler()),
        
        # Logistic regression classifier
        ('LogisticClassifier', LogisticRegression(random_state=0))
    ]
)
