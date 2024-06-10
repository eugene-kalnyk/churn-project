# Customer Churn Prediction Project

## Predictive Analytics for Customer Churn

This project is focused on predicting customer churn using a dataset obtained from [Kaggle](https://www.kaggle.com/datasets/safrin03/predictive-analytics-for-customer-churn-dataset). The dataset contains anonymized information about customer subscriptions and their interactions with the service. This includes various features such as subscription type, payment method, viewing preferences, customer support interactions, and other relevant attributes. The data is stored in the "data" folder and is named as: "train.csv", and "data_descriptions.csv".

A logistic regression model with balanced class weights is implemented for churn prediction. 

- ROC AUC score of the model is 0.7532.
- F1 score for class "0" is 0.78
- F1 score for class "1" is 0.44

## Installation

This application can be run using Python. 

Before using, follow the below steps to install the required dependencies and run the application:

1. Install the necessary libraries using pip, according to the provided requirements.txt file. In your terminal, navigate to the root directory of the project and run the following command:


`pip install -r requirements.txt`


2. Now, with all the dependencies installed, you're ready to run the app. In your terminal, execute the command:


`python app.py`


The application will start and should be accessible at  http://localhost:5000.

To get a prediction for a specific customer, make a GET request to the endpoint /predict with the customer ID as a query parameter. For example: http://localhost:5000/predict?q=customer-id

You can test the app using a sample test script in `scripts/test.py`.

You can find a list of customer IDs in the `data/test_CustomerID_Churn.csv` file.

## Running on Google Cloud

To deploy the app on Google Cloud, follow these steps:

1. **Create a Google Cloud Project**

    Go to the [Google Cloud Console](https://console.cloud.google.com/) and create a new project.

2. **Enable Google Cloud Run and Cloud Build APIs**

    Enable the required APIs for Cloud Run and Cloud Build.

3. **Dockerize the Application**

    Make sure you have a Dockerfile in the root directory of your project.

    ```Dockerfile
    # Use the official lightweight Python image.
    # https://hub.docker.com/_/python
    FROM python:3.10-slim

    # Allow statements and log messages to immediately appear in the Knative logs
    ENV PYTHONUNBUFFERED True

    # Copy local code to the container image.
    ENV APP_HOME /app
    WORKDIR $APP_HOME
    COPY . ./

    # Install production dependencies.
    RUN pip install --no-cache-dir -r requirements.txt

    # Install Gunicorn.
    RUN pip install gunicorn

    # Run the web service on container startup.
    CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
    ```

4. **Build and Push the Docker Image**

    Build and push the Docker image to the Google Container Registry:

    ```bash
    gcloud builds submit --tag gcr.io/your-project-id/churn-prediction
    ```

    Replace `your-project-id` with your actual Google Cloud Project ID.

5. **Deploy to Cloud Run**

    Deploy your Docker image to Google Cloud Run:

    ```bash
    gcloud run deploy churn-prediction --image gcr.io/your-project-id/churn-prediction --platform managed --region us-central1 --allow-unauthenticated
    ```

    Replace `your-project-id` with your actual Google Cloud Project ID.

6. **Access the Deployed App**

    Once deployed, you can access the app at the URL provided by Google Cloud Run. For example, https://churn-project-mzk3f6u53a-lm.a.run.app/predict.

    You can test the deployed app using the following script:

    ```python
    # scripts/test.py
    import requests

    url = "https://churn-project-mzk3f6u53a-lm.a.run.app/predict"
    params = {'q': "2X58V9435O"}
    response = requests.get(url, params=params)
    print(response.text)
    ```

## File and Directory Structure
├── README.md ├── requirements.txt ├── app.py ├── data │ ├── train.csv │ └── data_descriptions.csv ├── Dockerfile └── scripts └── test.py


- **README.md**: This file.
- **requirements.txt**: Lists the dependencies required for the project.
- **app.py**: Main application file.
- **data**: Folder containing the dataset.
  - **train.csv**: Training dataset.
  - **data_descriptions.csv**: Description of the dataset.
- **Dockerfile**: Instructions for Docker to create a container for the application.
- **scripts**: Folder containing scripts.
  - **test.py**: Script to test the API endpoint.