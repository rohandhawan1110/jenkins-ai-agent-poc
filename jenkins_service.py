import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os

load_dotenv()

JENKINS_URL = os.getenv("JENKINS_URL")
USERNAME = os.getenv("JENKINS_USER")
API_TOKEN = os.getenv("JENKINS_API_TOKEN")


# ---------------- GET CSRF CRUMB ----------------
def get_crumb():

    url = f"{JENKINS_URL}/crumbIssuer/api/json"

    response = requests.get(
        url,
        auth=HTTPBasicAuth(USERNAME, API_TOKEN)
    )

    data = response.json()

    return {
        data["crumbRequestField"]: data["crumb"]
    }


# ---------------- TRIGGER JOB ----------------
def trigger_job(job_name, params):

    url = f"{JENKINS_URL}/job/{job_name}/buildWithParameters"

    headers = get_crumb()

    response = requests.post(
        url,
        auth=HTTPBasicAuth(USERNAME, API_TOKEN),
        headers=headers,
        params=params
    )

    if response.status_code in [200, 201, 202]:
        print("✅ Jenkins job triggered successfully!")
    else:
        print("❌ Failed to trigger Jenkins")
        print(response.text)