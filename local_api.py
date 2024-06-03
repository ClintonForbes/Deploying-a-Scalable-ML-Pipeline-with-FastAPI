import json

import requests

# send a GET using the URL http://127.0.0.1:8000
url = "http://127.0.0.1:8000"
r = requests.get(url)

# print the status code
print(f"Status Code (GET): {r.status_code}")
# print the welcome message
print(f"Welcome Message (GET): {r.text}")



data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# send a POST using the data above
url_post = "http://127.0.0.1:8000/predict/"
headers = {"Content-Type": "application/json"}
r = requests.post(url_post, data=json.dumps(data), headers=headers)

# print the status code
print(f"\nStatus Code (POST): {r.status_code}")
# print the result
print(f"Prediction Result (POST): {r.json()}")
