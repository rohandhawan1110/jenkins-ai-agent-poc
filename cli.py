from ai_agent import process_confluence_page
from jenkins_service import trigger_job


def run_cli():

    print("\n🚀 AI Jenkins Agent CLI\n")

    input("\nPress Enter to process Confluence page...")

    data = process_confluence_page()

    if not data:
        print("❌ Failed to extract data from LLM")
        return

    print("\n🧠 Extracted Data:")
    print(data)

    job_name = data["job_name"]

    print(f"\n⚙️ Triggering Jenkins Job: {job_name}\n")

    trigger_job(
        data["job_name"],
        data["parameters"]
    )


if __name__ == "__main__":
    run_cli()