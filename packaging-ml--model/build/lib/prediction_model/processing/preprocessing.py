from sklearn.base import BaseEstimator, TransformerMixin
from pathlib import Path
import os
import sys

# Define the root directory of the package two levels up from the current file's directory
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent.parent

# Add the package root directory to the system path to allow importing from the prediction_model package
sys.path.append(str(PACKAGE_ROOT))

from prediction_model.config import config
import numpy as np

# Custom transformer for imputing missing values with the mean of the column
class MeanImputer(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None):
        self.variables = variables

    def fit(self, X, y=None):
        # Calculate the mean for each specified column and store it in a dictionary
        self.mean_dict = {}
        for col in self.variables:
            self.mean_dict[col] = X[col].mean()
        return self

    def transform(self, X):
        # Create a copy of the input dataframe
        X = X.copy()
        # Fill missing values with the mean for each specified column
        for col in self.variables:
            X[col].fillna(self.mean_dict[col], inplace=True)
        return X

# Custom transformer for imputing missing values with the mode of the column
class ModeImputer(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None):
        self.variables = variables

    def fit(self, X, y=None):
        # Calculate the mode for each specified column and store it in a dictionary
        self.mode_dict = {}
        for col in self.variables:
            self.mode_dict[col] = X[col].mode()[0]
        return self

    def transform(self, X):
        # Create a copy of the input dataframe
        X = X.copy()
        # Fill missing values with the mode for each specified column
        for col in self.variables:
            X[col].fillna(self.mode_dict[col], inplace=True)
        return X

# Custom transformer for dropping specified columns
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, variables_to_drop=None):
        self.variables_to_drop = variables_to_drop

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Create a copy of the input dataframe
        X = X.copy()
        # Drop the specified columns
        X = X.drop(columns=self.variables_to_drop)
        return X

# Custom transformer for domain-specific processing, e.g., modifying a variable by adding another variable
class DomainProcessing(BaseEstimator, TransformerMixin):
    def __init__(self, variable_to_modify=None, variable_to_add=None):
        self.variable_to_modify = variable_to_modify
        self.variable_to_add = variable_to_add

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Create a copy of the input dataframe
        X = X.copy()
        # Modify the specified variable by adding the value of another variable
        for feature in self.variable_to_modify:
            X[feature] = X[feature] + X[self.variable_to_add]
        return X

# Custom transformer for label encoding categorical features
class CustomLabelEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None):
        self.variables = variables

    def fit(self, X, y=None):
        # Create a dictionary for label encoding each specified column
        self.label_dict = {}
        for var in self.variables:
            t = X[var].value_counts().sort_values(ascending=True).index
            self.label_dict[var] = {k: i for i, k in enumerate(t, 0)}
        return self

    def transform(self, X):
        # Create a copy of the input dataframe
        X = X.copy()
        # Apply label encoding to each specified column
        for feature in self.variables:
            X[feature] = X[feature].map(self.label_dict[feature])
        return X

# Custom transformer for applying logarithmic transformation to numerical features
class LogTransforms(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None):
        self.variables = variables

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Create a copy of the input dataframe
        X = X.copy()
        # Apply logarithmic transformation to each specified column
        for col in self.variables:
            X[col] = np.log(X[col])
        return X
