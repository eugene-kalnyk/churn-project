This is a project to predict customer churn.
**Data source**: https://www.kaggle.com/datasets/safrin03/predictive-analytics-for-customer-churn-dataset

## Contents

### app (main folder)
- *Churn_smote.ipynb* — a jupyter lab notebook with model training
- *model.joblib* — a saved model
- *scaler.joblib* — a saved scaler
  
- *app.py* — a flask app for model deployment
- *Dockerfile* — a Docker file for model deployment
- *requirments.txt* — a python library versions for model deployment
- *test.py* — a file to connect to API and test the deployed model

### app/data
- *data_descriptions.csv* — column descriptions for the original dataset
- *test_CustomerID_Churn.csv* — the CustomerID and Churn values from the test portion of the dataset
- *train.csv* — the original dataset
