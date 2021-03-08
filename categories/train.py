import json
import ntpath
import requests
import sys
import time
import os

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

feature_to_train = "categories"
headers = {"Content-Type" : "multipart/form-data"}

data = {
    "name": "Email Workflow Categories #1",
    "language": "en",
    "version": "1.0.0"
}

params = {
    "version": "2021-03-07"
}

uri = $URL + "/v1/models/{}".format(feature_to_train)

print("\nCreating custom model...")
training_data_filename = "training_data.json"

with open("training_data_filename", "rb") as f:
    response = requests.post(
        params=params,
        data=data,
        files={"training_data": (ntpath.basename(training_data_filename), f, "application/json")},
        auth=(os.environ['USER'], os.environ['PASS']),
        verify=False,
    )

print("Model created: ", response.status_code)

if response.status_code != 201:
    print("Failed to create model")
    print(response.text)
else:
    print("\nCustom model training started...")
    response_json = response.json()
    model_id = response_json['model_id']
    print("Custom Model ID: ", model_id)
