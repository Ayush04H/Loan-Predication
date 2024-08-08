
# Loan Prediction Project

This project aims to predict the status of loan applications based on a dataset provided on Kaggle. The repository includes the implementation of a machine learning pipeline for training and predicting loan statuses, a FastAPI for serving predictions, and a Streamlit frontend for user interaction.

## Project Structure

The project is structured into various modules:

- **prediction_model/config**: Contains configuration files.
- **prediction_model/datasets**: Includes the training and testing datasets.
- **prediction_model/processing**: Contains data handling and preprocessing scripts.
- **prediction_model/trained_models**: Stores the trained model artifacts.
- **prediction_model**: Main module with pipeline and prediction scripts.
- **tests**: Contains unit tests for the prediction module.

## Dataset

The dataset used for this project can be found on Kaggle: [Loan Status Prediction Dataset](https://www.kaggle.com/datasets/bhavikjikadara/loan-status-prediction). It includes various features related to loan applications and their statuses.

##Data
The data corresponds to a set of financial requests associated with individuals. 

| Variables         | Description                                    |
|-------------------|------------------------------------------------|
| Loan_ID           | Unique Loan ID                                 |
| Gender            | Male/ Female                                   |
| Married           | Applicant married (Y/N)                        |
| Dependents        | Number of dependents                           |
| Education         | Applicant Education (Graduate/ Under Graduate) |
| Self_Employed     | Self employed (Y/N)                            |
| ApplicantIncome   | Applicant income                               |
| CoapplicantIncome | Coapplicant income                             |
| LoanAmount        | Loan amount in thousands                       |
| Loan_Amount_Term  | Term of loan in months                         |
| Credit_History    | credit history meets guidelines                |
| Property_Area     | Urban/ Semi Urban/ Rural                       |
| Loan_Status       | Loan approved (Y/N)                            |


## FastAPI

The project includes a FastAPI implementation for serving predictions. You can find more details in its [README.md file](https://github.com/Ayush04H/Loan-Predication/blob/main/packaging-ml--model/Loan_pred_Api/Readme.md).

## Streamlit Frontend

A Streamlit frontend is also provided for user interaction with the prediction model. More details are available in its [README.md file](https://github.com/Ayush04H/Loan-Predication/blob/main/packaging-ml--model/Loan_pred_frontend/Readme.md).

## Setup Instructions

To clone and set up the repository in a new virtual environment, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Ayush04H/Loan-Predication.git
    cd Loan-Predication
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

5. **Run the training pipeline**:
    ```sh
    python prediction_model/training_pipeline.py
    ```

6. **Make predictions**:
    ```sh
    python prediction_model/predict.py
    ```

## Docker Setup

To build and run the project using Docker, follow these steps:
    ```

1. **Commands to run Docker on any system**:
    ```sh
    docker login
    docker pull ayush04h/loan-prediction-model
    docker run -p 8501:8501 ayush04h/loan-prediction-model
    ```
