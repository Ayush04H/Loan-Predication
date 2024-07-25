# Loan Eligibility Prediction App

This repository contains a Streamlit web application designed to predict loan eligibility based on user input. The app utilizes a pre-trained machine learning model to make predictions and display whether a loan application is approved or rejected.

## Overview

The application is built using Streamlit, a popular framework for creating web applications with Python. It uses a pre-trained classification model to evaluate loan eligibility based on various features provided by the user.

### Features

- **Gender**: Select from "Male" or "Female".
- **Married**: Choose between "Yes" or "No".
- **Dependents**: Select the number of dependents ("0", "1", "2", "3+").
- **Education**: Choose between "Graduate" or "Not Graduate".
- **Self Employed**: Choose between "Yes" or "No".
- **Applicant Income**: Enter the applicant's income.
- **Coapplicant Income**: Enter the coapplicant's income.
- **Loan Amount**: Enter the amount of the loan.
- **Loan Amount Term**: Enter the term of the loan in months.
- **Credit History**: Select between 0 (no credit history) and 1 (credit history exists).
- **Property Area**: Select from "Urban", "Semiurban", or "Rural".

### Requirements

- Python 3.x
- Streamlit
- Pandas
- Numpy
- Joblib
- Additional libraries may be required as specified in the `prediction_model` package.

### How It Works

1. **Imports and Setup**: The necessary libraries are imported, including Streamlit for the web interface, Pandas and Numpy for data manipulation, and Joblib for loading the pre-trained model. The package path is configured to ensure the model can be loaded correctly.

2. **Model Loading**: The pre-trained classification pipeline is loaded using the `load_pipeline` function from the `prediction_model.processing.data_handling` module. If there is an error loading the model, an error message is displayed in the Streamlit app.

3. **User Input**: The app presents input fields for various features related to loan eligibility. Input validation is handled with try-except blocks to catch and display any errors in user input.

4. **Prediction Generation**: When the "Predict" button is pressed, the input data is collected into a dictionary and passed to the `generate_predictions` function. This function creates a DataFrame from the input data, makes predictions using the loaded model, and returns the result.

5. **Display Results**: Based on the prediction result, the app displays either a success or error message indicating whether the loan status is approved or rejected.

### Running the Application

1. **Install Dependencies**: Ensure that all required libraries are installed. You can typically install these using `pip`:
    ```bash
    pip install streamlit pandas numpy joblib
    ```

2. **Run the Application**: Execute the Streamlit app using the following command:
    ```bash
    streamlit run app.py
    ```

3. **Access the App**: Open a web browser and navigate to the URL provided by Streamlit, usually `http://localhost:8501`.

### Troubleshooting

- **Model Loading Error**: Check the path and filename of the model specified in `config.MODEL_NAME`. Ensure that the model file is present and accessible.
- **Input Errors**: Verify the input values and ensure they conform to the expected types and ranges.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize the app further and enhance its features as needed!
