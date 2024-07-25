# Loan Prediction API

## Overview

This FastAPI application provides an endpoint for predicting loan approval status based on user input. The model predicts whether a loan application should be accepted or rejected. 

## Code Description

- **`loan_pred_api.py`**: This file contains the FastAPI application code. It defines the API endpoint `/predict`, which accepts loan application data and returns the loan status.

- **`prediction_model`**:
  - **`config.py`**: Contains configuration settings, including file paths and feature definitions.
  - **`processing`**:
    - **`data_handling.py`**: Functions for loading and saving the model pipeline.
    - **`preprocessing.py`**: Functions for data preprocessing (not used in the current example).
  - **`predict.py`**: Contains the function `generate_predictions` that uses the loaded model to make predictions.

## Running the Application

1. **Install Dependencies**: Make sure you have the required Python packages installed. You can use `pip` to install them:
    ```bash
    pip install fastapi uvicorn pandas joblib
    ```

2. **Run the FastAPI Server**:
    Navigate to the directory containing `loan_pred_api.py` and run the following command:
    ```bash
    uvicorn loan_pred_api:app --reload
    ```

    The server will start, and you can access the API at `http://127.0.0.1:8000`.

## Testing the API

### Using Swagger UI

1. **Open Swagger UI**:
   - Go to `http://127.0.0.1:8000/docs` in your web browser.

2. **Test the API**:
   - Find the `/predict` endpoint in the list.
   - Click on the "Try it out" button.
   - Enter the loan application data in JSON format into the request body. For example:
     ```json
     {
       "Gender": "Male",
       "Married": "No",
       "Dependents": "1",
       "Education": "Graduate",
       "Self_Employed": "No",
       "ApplicantIncome": 4000,
       "CoapplicantIncome": 2000,
       "LoanAmount": 150,
       "Loan_Amount_Term": 300,
       "Credit_History": 1,
       "Property_Area": "Rural"
     }
     ```

     ```json
     {
      "Gender": "Male",
      "Married": "No",
      "Dependents": "1",
      "Education": "Graduate",
      "Self_Employed": "No",
      "ApplicantIncome": 4000,
      "CoapplicantIncome": 2000,
      "LoanAmount": 150,
      "Loan_Amount_Term": 300,
      "Credit_History": 1,
      "Property_Area": "Rural"
      }

     ```

     ```json
     {
      "Gender": "Female",
      "Married": "Yes",
      "Dependents": "2",
      "Education": "Not Graduate",
      "Self_Employed": "Yes",
      "ApplicantIncome": 5000,
      "CoapplicantIncome": 1000,
      "LoanAmount": 200,
      "Loan_Amount_Term": 360,
      "Credit_History": 1,
      "Property_Area": "Urban"
      }

     ```

     ```json
     {
      "Gender": "Male",
      "Married": "Yes",
      "Dependents": "0",
      "Education": "Graduate",
      "Self_Employed": "No",
      "ApplicantIncome": 3000,
      "CoapplicantIncome": 1500,
      "LoanAmount": 120,
      "Loan_Amount_Term": 240,
      "Credit_History": 0,
      "Property_Area": "Semiurban"
      }

     ```

     ```json
     {
      "Gender": "Female",
      "Married": "No",
      "Dependents": "3+",
      "Education": "Graduate",
      "Self_Employed": "Yes",
      "ApplicantIncome": 4500,
      "CoapplicantIncome": 0,
      "LoanAmount": 100,
      "Loan_Amount_Term": 180,
      "Credit_History": 1,
      "Property_Area": "Rural"
      }

     ```

     ```json
     {
      "Gender": "Male",
      "Married": "Yes",
      "Dependents": "1",
      "Education": "Not Graduate",
      "Self_Employed": "No",
      "ApplicantIncome": 3500,
      "CoapplicantIncome": 1800,
      "LoanAmount": 170,
      "Loan_Amount_Term": 300,
      "Credit_History": 0,
      "Property_Area": "Urban"
      }

     ```

     
   - Click the "Execute" button to send the request.

3. **View the Response**:
   - The response will be displayed below, showing the loan status (e.g., "Accepted" or "Rejected").

### Using Postman

1. **Open Postman**:
   - Launch Postman application on your machine.

2. **Create a New Request**:
   - Click on the "New" button and select "Request".

3. **Set the Request Type and URL**:
   - Change the request type to `POST`.
   - Enter `http://127.0.0.1:8000/predict` in the URL field.

4. **Set the Request Body**:
   - Click on the "Body" tab.
   - Select "raw" and choose "JSON" from the dropdown menu.
   - Enter the loan application data in JSON format as shown above.

5. **Send the Request**:
   - Click on the "Send" button.

6. **View the Response**:
   - The response will be displayed in the lower section of Postman, showing whether the loan status is "Accepted" or "Rejected".

## Author

- **Ayush Kumar Srivastava**
