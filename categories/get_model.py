import requests
import os
import json

from dotenv import load_dotenv
load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
from pathlib import Path  # Python 3.6+ only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

headers = {"Content-Type" : "multipart/form-data"}
params = {
    "version": "2021-03-07"
}

model_uri = os.getenv("URL") + "/v1/models/categories/" + os.getenv("MODEL_ID")
response = requests.get(model_uri,
    auth=(os.getenv("USER"), os.getenv("PASS")),
    params=params,
    verify=False,
    headers=headers
)

print("Model retrieved: ", response.status_code)
response_json = response.json()
print("Response from NLU:\n", json.dumps(response_json, indent=4, sort_keys=True))
