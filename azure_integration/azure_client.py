import os
import requests
import base64
from bs4 import BeautifulSoup
from config.settings import AZURE_DEVOPS_URL, AZURE_DEVOPS_ORG, AZURE_DEVOPS_PROJECT, AZURE_DEVOPS_PAT

class AzureClient:
    def fetch_azure_work_items(self, work_item_ids=None):
        if not work_item_ids:
            work_item_ids = os.getenv("AZURE_DEVOPS_WORKITEM_IDS", "").split(",")
            work_item_ids = [id.strip() for id in work_item_ids if id.strip()]

        if not work_item_ids:
            print("⚠️ Work item IDs not found. Please set AZURE_DEVOPS_WORKITEM_IDS in your .env file.")
            return None

        results = []
        for work_item_id in work_item_ids:
            url = f"{AZURE_DEVOPS_URL}/{AZURE_DEVOPS_ORG}/{AZURE_DEVOPS_PROJECT}/_apis/wit/workitems/{work_item_id}?api-version=6.0"
            headers = {
                "Accept": "application/json",
                "Authorization": f"Basic {base64.b64encode(f':{AZURE_DEVOPS_PAT}'.encode()).decode()}"
            }

            try:
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    work_item = response.json()
                    
                    # Clean HTML tags from the description
                    def clean_html(text):
                        soup = BeautifulSoup(text, "html.parser")
                        return soup.get_text()

                    description = work_item.get("fields", {}).get("System.Description", "No Description Found")
                    description_cleaned = clean_html(description)
                    title = work_item.get("fields", {}).get("System.Title", "No Title Found")
                    
                    results.append({
                        "id": work_item_id,
                        "title": title,
                        "description": description_cleaned
                    })
                    print(f"✅ Successfully fetched work item {work_item_id}")
                else:
                    print(f"❌ Failed to fetch work item {work_item_id}: {response.status_code}")
            except Exception as e:
                print(f"❌ Error processing work item {work_item_id}: {str(e)}")

        return results