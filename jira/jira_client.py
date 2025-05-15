import requests
from typing import Optional, Dict, Any
from config.settings import JIRA_URL, JIRA_USER, JIRA_API_TOKEN

def fetch_issue(issue_key: str) -> Optional[Dict[str, Any]]:
    """Fetch issue details from Jira.

    Args:
        issue_key (str): The Jira issue key

    Returns:
        Optional[Dict[str, Any]]: Issue details or None if fetch fails
    """
    if not issue_key:
        print("❌ Issue key cannot be empty")
        return None

    url = f"{JIRA_URL}/rest/api/3/issue/{issue_key}"
    headers = {"Accept": "application/json"}

    try:
        response = requests.get(
            url,
            auth=(JIRA_USER, JIRA_API_TOKEN),
            headers=headers,
            timeout=30  # Add timeout
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to fetch issue: {e}")
        return None
    except requests.exceptions.JSONDecodeError as e:
        print(f"❌ Error decoding JSON: {e}")
        return None
