from ai_agent import process_confluence_page
from jenkins_service import trigger_job


def run_cli():

    print("\n🚀 AI Jenkins Agent CLI\n")

    confluence_url = input("\nEnter Confluence URL: ")
    page_id = confluence_url.split("/pages/")[1].split("/")[0]

    data = process_confluence_page(page_id)

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