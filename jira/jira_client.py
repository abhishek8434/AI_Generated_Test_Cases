import requests
from config.settings import JIRA_URL, JIRA_USER, JIRA_API_TOKEN

def fetch_issue(issue_key):
    url = f"{JIRA_URL}/rest/api/3/issue/{issue_key}"
    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url, auth=(JIRA_USER, JIRA_API_TOKEN), headers=headers)

    if response.status_code != 200:
        print(f"❌ Failed to fetch issue: {response.status_code}")
        print(f"Response Text:\n{response.text}")
        return None

    try:
        return response.json()
    except requests.exceptions.JSONDecodeError as e:
        print("❌ Error decoding JSON:")
        print(response.text)
        return None
