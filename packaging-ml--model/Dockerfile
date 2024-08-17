# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Train the model
RUN python prediction_model/training_pipeline.py

# Expose port for the frontend
EXPOSE 8501

# Run the frontend
CMD ["streamlit", "run", "Loan_pred_frontend/loanpred_frontend.py"]
