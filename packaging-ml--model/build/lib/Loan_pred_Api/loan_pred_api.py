from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Any
import pandas as pd

from prediction_model.config import config
from prediction_model.processing.data_handling import load_pipeline

# Load the pre-trained model pipeline
classification_pipeline = load_pipeline(config.MODEL_NAME)

app = FastAPI()

# Define the request model
class LoanApplication(BaseModel):
    Gender: str
    Married: str
    Dependents: str
    Education: str
    Self_Employed: str
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    Property_Area: str

@app.post("/predict")
async def predict_loan_status(application: LoanApplication):
    try:
        # Convert the input data to a DataFrame
        data = pd.DataFrame([application.dict()])
        
        # Generate predictions
        predictions = classification_pipeline.predict(data[config.FEATURES])
        output = 'Y' if predictions[0] == 1 else 'N'
        
        return {"prediction": output}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
