import requests

url = "https://churn-project-mzk3f6u53a-lm.a.run.app/predict"

params = {
    'q':"2X58V9435O"
}

answer = requests.get(url, params=params)

print(answer.text)