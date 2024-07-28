import pathlib
import os
import prediction_model

# Define the root directory of the prediction_model package
PACKAGE_ROOT = pathlib.Path(prediction_model.__file__).resolve().parent
print(PACKAGE_ROOT)

# Define the path to the datasets directory within the package
DATAPATH = os.path.join(PACKAGE_ROOT, "datasets")

# Define the filenames for the training and test datasets
TRAIN_FILE = 'train.csv'
TEST_FILE = 'test.csv'

# Define the name of the model file to be saved
MODEL_NAME = 'classification.pkl'

# Define the path to the directory where the trained models will be saved
SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT, 'trained_models')

# Define the target variable for the model
TARGET = 'Loan_Status'

# List of features to be used in the model
FEATURES = ['Gender', 'Married', 'Dependents', 'Education',
            'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
            'Loan_Amount_Term', 'Credit_History', 'Property_Area']

# List of numerical features
NUM_FEATURES = ['ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term']

# List of categorical features
CAT_FEATURES = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 
                'Credit_History', 'Property_Area']

# List of features to encode (same as categorical features in this case)
FEATURES_TO_ENCODE = ['Gender', 'Married', 'Dependents', 'Education', 
                      'Self_Employed', 'Credit_History', 'Property_Area']

# Feature to be modified (e.g., transformed)
FEATURE_TO_MODIFY = ['ApplicantIncome']

# Feature to be added
FEATURE_TO_ADD = 'CoapplicantIncome'

# Features to drop (e.g., to avoid multicollinearity)
DROP_FEATURES = ['CoapplicantIncome']

# Features to apply logarithmic transformation to (for normalization purposes)
LOG_FEATURES = ['ApplicantIncome', 'LoanAmount']
