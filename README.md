# AI Jenkins Agent POC

## Overview

AI Jenkins Agent is a Proof of Concept (POC) that automates Jenkins job execution using information stored in Confluence pages.

The solution reads a Confluence page, extracts deployment details using an LLM (Ollama + Llama3), converts the information into structured JSON, and triggers the corresponding Jenkins job automatically.

---

## Problem Statement

Teams often receive deployment requests through Confluence pages or documentation.

Engineers must manually:

1. Read the Confluence page
2. Identify the Jenkins job
3. Identify deployment parameters
4. Trigger the Jenkins pipeline

This process is repetitive and prone to human error.

---

## Solution

The AI Jenkins Agent automates the workflow:

Confluence Page → AI Extraction → Structured JSON → Jenkins Trigger

Example Confluence Content:

Jenkins Job: CustomerPortal_Build

Environment: UAT

Branch: main

Extracted JSON:

```json
{
  "job_name": "CustomerPortal_Build",
  "environment": "UAT",
  "branch": "main"
}
```

The solution then triggers the Jenkins job with the extracted parameters.

---

## Architecture

```text
User / CLI
     |
     v
Confluence API
     |
     v
HTML Cleaning
     |
     v
Ollama (Llama3)
     |
     v
Structured JSON
     |
     v
Jenkins API
     |
     v
Pipeline Execution
```

---

## Project Structure

```text
jenkins-ai-agent/

├── ai_agent.py
├── cli.py
├── config.py
├── jenkins_service.py
├── requirements.txt
├── .env.template
└── README.md
```

### File Responsibilities

| File               | Purpose                                      |
| ------------------ | -------------------------------------------- |
| ai_agent.py        | Confluence fetch, cleaning and AI processing |
| cli.py             | Command-line entry point                     |
| config.py          | Configuration and environment variables      |
| jenkins_service.py | Jenkins integration                          |
| .env.template      | Sample environment configuration             |

---

## Prerequisites

* Python 3.10+
* Jenkins
* Confluence Cloud
* Ollama
* Llama3 model

Install Ollama:

https://ollama.com

Pull Llama3:

```bash
ollama pull llama3
```

---

## Installation

Clone repository:

```bash
git clone https://github.com/rohandhawan1110/jenkins-ai-agent-poc.git

cd jenkins-ai-agent-poc
```

Create virtual environment:

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file using `.env.template`.

Example:

```env
CONFLUENCE_URL=https://your-domain.atlassian.net/wiki

CONFLUENCE_USERNAME=your_email

CONFLUENCE_API_TOKEN=your_token

CONFLUENCE_PAGE_ID=123456

JENKINS_URL=http://localhost:8080

JENKINS_USER=admin

JENKINS_API_TOKEN=your_token
```

---

## Running the Application

Start Ollama:

```bash
ollama serve
```

Run the CLI:

```bash
python cli.py
```

---

## Current Scope (POC)

Implemented:

* Confluence page retrieval
* HTML cleaning
* LLM-based data extraction
* JSON conversion
* Jenkins job triggering
* CLI interface

Planned Enhancements:

* FastAPI REST API
* Web UI
* Dynamic Confluence page selection
* Multi-job mapping
* Validation and approval workflow
* Azure OpenAI integration

---

## Author

Rohan Dhawan

AI-driven Jenkins Automation POC
