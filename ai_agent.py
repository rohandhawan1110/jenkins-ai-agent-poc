import requests
import json
import ollama
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth
import re

from config import (
    CONFLUENCE_BASE_URL,
    CONFLUENCE_USERNAME,
    CONFLUENCE_API_TOKEN,
    CONFLUENCE_PAGE_ID
)

# ---------------- FETCH ----------------
def fetch_confluence():
    url = f"{CONFLUENCE_BASE_URL}/rest/api/content/{CONFLUENCE_PAGE_ID}?expand=body.storage"

    response = requests.get(
        url,
        auth=HTTPBasicAuth(CONFLUENCE_USERNAME, CONFLUENCE_API_TOKEN)
    )

    return response.json()["body"]["storage"]["value"]


# ---------------- CLEAN ----------------
def clean_html(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text("\n")


# ---------------- LLM ----------------
def extract_with_llm(text):

    prompt = f"""
You are a STRICT JSON generator.

RULES:
- Output ONLY valid JSON
- NO explanation
- NO markdown
- NO text before or after JSON
- Extract ALL deployment parameters except Jenkins Job.
- Place them inside the parameters object.

OUTPUT FORMAT:
{{
  "job_name": "",
  "parameters": {{
    "key": "value"
  }}
}}

INPUT:
{text}
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]


# ---------------- PIPELINE ----------------
def process_confluence_page():

    html = fetch_confluence()

    text = clean_html(html)

    llm_output = extract_with_llm(text)

    print("\nRAW LLM OUTPUT:\n", llm_output)

    try:
        return json.loads(llm_output)
    except:
        pass

    # fallback: extract JSON block
    match = re.search(r"\{.*\}", llm_output, re.DOTALL)

    if match:
        try:
            return json.loads(match.group())
        except:
            return None

    return None