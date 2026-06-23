import requests
from requests.auth import HTTPBasicAuth
from config import JENKINS_URL, JENKINS_USER, JENKINS_API_TOKEN


def trigger_job(job_name, params):

    url = f"{JENKINS_URL}/job/{job_name}/buildWithParameters"

    response = requests.post(
        url,
        auth=HTTPBasicAuth(JENKINS_USER, JENKINS_API_TOKEN),
        params=params
    )

    if response.status_code in [200, 201, 202]:
        print("✅ Jenkins triggered successfully")
    else:
        print("❌ Jenkins trigger failed")
        print(response.text)