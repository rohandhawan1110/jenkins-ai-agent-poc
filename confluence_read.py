import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv

# Load credentials from .env
load_dotenv()

CONFLUENCE_URL = os.getenv("CONFLUENCE_URL")
USERNAME = os.getenv("CONFLUENCE_USERNAME")
API_TOKEN = os.getenv("CONFLUENCE_API_TOKEN")
page_id = os.getenv("CONFLUENCE_PAGE_ID")

url = f"{CONFLUENCE_URL}/rest/api/content/{page_id}?expand=body.storage"

response = requests.get(url, auth=(USERNAME, API_TOKEN))

if response.status_code == 200:
    content = response.json()
    page_body = content["body"]["storage"]["value"]
    print("Page content fetched successfully!\n")
    print(page_body)
else:
    print("Failed to fetch page:", response.status_code, response.text)

# with open("sample_wiki.txt") as file:
#     content = file.read()
# print(content)