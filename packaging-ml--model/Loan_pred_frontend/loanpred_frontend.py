import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
import os
import sys

# Define the root directory of the package one level up from the current file's directory
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent

# Add the package root directory to the system path to allow importing from the prediction_model package
sys.path.append(str(PACKAGE_ROOT))

from prediction_model.config import config  
from prediction_model.processing.data_handling import load_pipeline

# Load the pre-trained classification pipeline from the specified model file
try:
    classification_pipeline = load_pipeline(config.MODEL_NAME)
except Exception as e:
    st.error(f"Error loading the model: {e}")

# Define the function to generate predictions
def generate_predictions(data_input):
    try:
        data = pd.DataFrame(data_input)
        pred = classification_pipeline.predict(data[config.FEATURES])
        output = np.where(pred == 1, 'Y', 'N')
        result = {"prediction": output}
        return result
    except Exception as e:
        st.error(f"Error generating predictions: {e}")
        return None

# Streamlit app
st.title("🏦 Loan Eligibility Prediction 🏦")

# Input fields for the features with try-except blocks
try:
    Gender = st.selectbox("Gender", ["Male", "Female"])
except Exception as e:
    st.error(f"Error with input Gender: {e}")

try:
    Married = st.selectbox("Married", ["Yes", "No"])
except Exception as e:
    st.error(f"Error with input Married: {e}")

try:
    Dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
except Exception as e:
    st.error(f"Error with input Dependents: {e}")

try:
    Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
except Exception as e:
    st.error(f"Error with input Education: {e}")

try:
    Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])
except Exception as e:
    st.error(f"Error with input Self_Employed: {e}")

try:
    ApplicantIncome = st.number_input("Applicant Income", min_value=0)
except Exception as e:
    st.error(f"Error with input Applicant Income: {e}")

try:
    CoapplicantIncome = st.number_input("Coapplicant Income", min_value=0)
except Exception as e:
    st.error(f"Error with input Coapplicant Income: {e}")

try:
    LoanAmount = st.number_input("Loan Amount", min_value=0)
except Exception as e:
    st.error(f"Error with input Loan Amount: {e}")

try:
    Loan_Amount_Term = st.number_input("Loan Amount Term", min_value=0)
except Exception as e:
    st.error(f"Error with input Loan Amount Term: {e}")

try:
    Credit_History = st.selectbox("Credit History", [0, 1])
except Exception as e:
    st.error(f"Error with input Credit History: {e}")

try:
    Property_Area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])
except Exception as e:
    st.error(f"Error with input Property Area: {e}")

# Collect input data into a dictionary
input_data = {
    "Gender": [Gender],
    "Married": [Married],
    "Dependents": [Dependents],
    "Education": [Education],
    "Self_Employed": [Self_Employed],
    "ApplicantIncome": [ApplicantIncome],
    "CoapplicantIncome": [CoapplicantIncome],
    "LoanAmount": [LoanAmount],
    "Loan_Amount_Term": [Loan_Amount_Term],
    "Credit_History": [Credit_History],
    "Property_Area": [Property_Area]
}

# Custom CSS for button styling
st.markdown("""
    <style>
    .stButton button {
        background-color: #6a0dad; /* Purple color */
        color: #000000; /* Black text color */
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #5c0ba1; /* Darker purple on hover */
    }
    </style>
    """, unsafe_allow_html=True)

# Button to get predictions
if st.button("Predict"):
    prediction = generate_predictions(input_data)
    if prediction:
        if prediction["prediction"][0] == 'Y':
            st.success("Loan Status Approved", icon="✅")
        else:
            st.error("Loan Status Rejected", icon="❌")

# Command to run the app
#if __name__ == '__main__':
#    os.system('streamlit run app.py')
