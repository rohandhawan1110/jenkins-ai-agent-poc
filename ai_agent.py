import os
import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth
import ollama
from dotenv import load_dotenv
from jenkins_service import trigger_job
import json

load_dotenv()

# ---------------- CONFIG ----------------
BASE_URL = os.getenv("CONFLUENCE_URL")
USERNAME = os.getenv("CONFLUENCE_USERNAME")
API_TOKEN = os.getenv("CONFLUENCE_API_TOKEN")
PAGE_ID = os.getenv("CONFLUENCE_PAGE_ID")


# ---------------- STEP 1: FETCH CONFLUENCE ----------------
def fetch_confluence():
    url = f"{BASE_URL}/rest/api/content/{PAGE_ID}?expand=body.storage"

    response = requests.get(
        url,
        auth=HTTPBasicAuth(USERNAME, API_TOKEN)
    )

    data = response.json()

    html = data["body"]["storage"]["value"]
    return html


# ---------------- STEP 2: CLEAN HTML ----------------
def clean_html(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text("\n")


# ---------------- STEP 3: LLM EXTRACTION ----------------
def extract_with_llm(text):
    prompt = f"""
You are a strict JSON generator for automation.

RULES:
- Return ONLY valid JSON
- NO explanations
- NO markdown
- NO ``` backticks
- NO extra text

TEXT:
{text}

OUTPUT FORMAT:
{{
  "job_name": "",
  "environment": "",
  "branch": ""
}}
"""

    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]


# ---------------- MAIN PIPELINE ----------------
if __name__ == "__main__":

    print("Fetching Confluence page...")
    html = fetch_confluence()

    print("\nCleaning HTML...")
    text = clean_html(html)
    print("Clean text: ", text)

    print("\nSending to LLM...")
    result = extract_with_llm(text)

    print("\nFINAL OUTPUT:")
    print("\nRaw LLM Output:\n", result)

    try:
        parsed = json.loads(result)
    except:
        print("❌ Invalid JSON from LLM")
        parsed = None


    if parsed:
        print("\nTriggering Jenkins...")

        trigger_job(
            parsed["job_name"],
            {
                "environment": parsed["environment"],
                "branch": parsed["branch"]
            }
        )