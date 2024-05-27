import requests

url = "https://churn-project-mzk3f6u53a-lm.a.run.app/predict"

params = {
    'q':"VNQUDIIEXS"
}

answer = requests.get(url, params=params)

print(answer.text)