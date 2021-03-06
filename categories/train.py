import json
import ntpath
import requests
import sys
import time
import os

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from dotenv import load_dotenv
load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
from pathlib import Path  # Python 3.6+ only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

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

uri = os.getenv("URL") + "/v1/models/{}".format(feature_to_train)

print("\nCreating custom model...")
training_data_filename = "training_data.json"

with open(training_data_filename, "rb") as f:
    response = requests.post(uri,
        params=params,
        data=data,
        files={"training_data": (ntpath.basename(training_data_filename), f, "application/json")},
        auth=(os.getenv("USER"), os.getenv("PASS")),
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
    model_uri = os.getenv("URL") + "/v1/models/categories/" + model_id
    response = requests.get(model_uri,
        auth=(os.getenv("USER"), os.getenv("PASS")),
        params=params,
        verify=False,
        headers=headers
    )

    print("Model retrieved: ", response.status_code)
    response_json = response.json()
    print("Response from NLU:\n", json.dumps(response_json, indent=4, sort_keys=True))
