
import pandas as pd
from flask import Flask, request, jsonify
from joblib import load

app = Flask(__name__)

# Load the trained model and the scaler
lr = load(open('models/model.joblib', 'rb'))
scaler = load(open('models/scaler.joblib', 'rb'))

# Load the dataframe
train_df = pd.read_csv('data/train.csv')

def process_data(train_df):
    df_num = train_df.copy()
    # Select categorical columns
    cat_cols = df_num.select_dtypes(include=['object']).columns
    cat_cols = cat_cols.drop('CustomerID')

    # Let's create dummies
    for col in cat_cols:
        df_num = pd.get_dummies(df_num, columns=[col])
    
    df_processed = df_num.drop('CustomerID', axis=1)
    return df_processed

df_processed = process_data(train_df)


@app.route('/predict', methods=['GET'])
def predict():
    customer_id = request.args.get('q')
    customer = train_df[train_df['CustomerID'] == customer_id]
    
    if customer.empty:
        return jsonify("CustomerID not found in the data")

    # preprocess data to match model's input
    customer_preprocessed = pd.get_dummies(customer.drop('CustomerID', axis=1))
    missing_cols = set(df_processed.columns) - set(customer_preprocessed.columns)

    for c in missing_cols:
        customer_preprocessed[c] = 0

    customer_preprocessed = customer_preprocessed[df_processed.columns]
  
    customer_features = customer_preprocessed.drop('Churn', axis=1)
    customer_target = customer_preprocessed['Churn']

    customer_features_scaled = scaler.transform(customer_features)
    prediction = lr.predict(customer_features_scaled)
    output = str(int(prediction[0]))
    return jsonify(output)

if __name__ == '__main__':
    app.run(port=5000, debug=True)