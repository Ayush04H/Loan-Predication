import pathlib
import os
import prediction_model

Package_root=pathlib.Path(prediction_model.__file__).resolve().parent
Datapath=os.path.join(Package_root,"datasets")

Train_file='train..csv'
Test_file='test.csv'

Saved_Model=os.path.join(Package_root,"trained_model")

Target='Loan_Status'

# Final Features Used In A Model
Features=['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
       'ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History',
       'Property_Area']

Num_features=['ApplicantIncome', 'LoanAmount',
       'Loan_Amount_Term']

Cat_features=['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
         'Credit_History', 'Property_Area']

# Features to Encode
Features_to_encode=['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
         'Credit_History', 'Property_Area'] 

Feature_to_modify=['ApplicantIncome']
Feature_to_add='CoApplicantIncome'

Drop_features=['CoApplicantIncome']

Log_features=['ApplicantIncome', 'LoanAmount']