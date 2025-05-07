import os
import requests
import base64
from bs4 import BeautifulSoup
from config.settings import AZURE_DEVOPS_URL, AZURE_DEVOPS_ORG, AZURE_DEVOPS_PROJECT, AZURE_DEVOPS_PAT

class AzureClient:
    def fetch_azure_work_item(self):  # Instance method to fetch work item details
        work_item_id = os.getenv("AZURE_DEVOPS_WORKITEM_ID")
        if not work_item_id:
            print("⚠️ Work item ID not found in environment. Please set AZURE_DEVOPS_WORKITEM_ID in your .env file.")
            return None

        url = f"{AZURE_DEVOPS_URL}/{AZURE_DEVOPS_ORG}/{AZURE_DEVOPS_PROJECT}/_apis/wit/workitems/{work_item_id}?api-version=6.0"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Basic {base64.b64encode(f':{AZURE_DEVOPS_PAT}'.encode()).decode()}"
        }
    
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            try:
                work_item = response.json()

                # Clean HTML tags from the description
                def clean_html(text):
                    soup = BeautifulSoup(text, "html.parser")
                    return soup.get_text()

                description = work_item.get("fields", {}).get("System.Description", "No Description Found")
                description_cleaned = clean_html(description)

                title = work_item.get("fields", {}).get("System.Title", "No Title Found")

                # print(f"📝 Title: {title}")
                # print(f"📄 Description: {description_cleaned}")
                
                return {"title": title, "description": description_cleaned}
            except requests.exceptions.JSONDecodeError as e:
                print("❌ Error decoding JSON:")
                print(response.text)
                return None
        else:
            print(f"❌ Failed to fetch work item: {response.status_code}")
            print(f"Response Text:\n{response.text}")
            return None