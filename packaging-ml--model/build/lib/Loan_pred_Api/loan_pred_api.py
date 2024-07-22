from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import pandas as pd
import sys
from pathlib import Path
import os

# Adjust the import path
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

from prediction_model.config import config  
from prediction_model.processing.data_handling import load_pipeline
from prediction_model.predict import generate_predictions

app = FastAPI()

# Author: Ayush Kumar Srivastava

# Define the request model using Pydantic
class LoanApplication(BaseModel):
    Gender: str
    Married: str
    Dependents: str
    Education: str
    Self_Employed: str
    ApplicantIncome: int
    CoapplicantIncome: int
    LoanAmount: int
    Loan_Amount_Term: int
    Credit_History: float
    Property_Area: str

# Load the classification model
try:
    classification_pipeline = load_pipeline(config.MODEL_NAME)
except FileNotFoundError as e:
    raise RuntimeError(f"Model file not found: {e}")
except Exception as e:
    raise RuntimeError(f"Error loading the model: {e}")

@app.post("/predict")
def predict_loan_status(application: LoanApplication):
    """
    Predict the loan status based on the input loan application data.
    
    Args:
    application: LoanApplication - Loan application data model.
    
    Returns:
    JSON response with the loan status ("Accepted" or "Rejected").
    """
    try:
        # Convert the input to a DataFrame
        application_data = application.dict()
        data = pd.DataFrame([application_data])
        
        # Generate prediction using the loaded pipeline
        prediction = generate_predictions(data)
        
        # Determine loan status based on the prediction
        loan_status = "Accepted" if prediction["prediction"][0] == "Y" else "Rejected"
        return {"loan_status": loan_status}
    
    except KeyError as e:
        raise HTTPException(status_code=422, detail=f"Missing data: {e}")
    except ValueError as e:
        raise HTTPException(status_code=422, detail=f"Invalid value: {e}")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
