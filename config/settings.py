import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
JIRA_URL = os.getenv("JIRA_URL")
JIRA_USER = os.getenv("JIRA_USER")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
BASE_URL = os.getenv("BASE_URL")

# Environment Variables
AZURE_DEVOPS_URL = os.getenv("AZURE_DEVOPS_URL")
AZURE_DEVOPS_ORG = os.getenv("AZURE_DEVOPS_ORG")
AZURE_DEVOPS_PROJECT = os.getenv("AZURE_DEVOPS_PROJECT")
AZURE_DEVOPS_PAT = os.getenv("AZURE_DEVOPS_PAT")
AZURE_DEVOPS_WORKITEM_ID = os.getenv("AZURE_DEVOPS_WORKITEM_ID")


# Check for missing variables
required_vars = [
    AZURE_DEVOPS_URL, AZURE_DEVOPS_ORG, AZURE_DEVOPS_PROJECT, 
    AZURE_DEVOPS_PAT, AZURE_DEVOPS_WORKITEM_ID, BASE_URL,
    JIRA_URL, JIRA_USER, JIRA_API_TOKEN
]

missing_vars = [name for name, value in zip([
    "AZURE_DEVOPS_URL", "AZURE_DEVOPS_ORG", "AZURE_DEVOPS_PROJECT", 
    "AZURE_DEVOPS_PAT", "AZURE_DEVOPS_WORKITEM_ID", "BASE_URL",
    "JIRA_URL", "JIRA_USER", "JIRA_API_TOKEN"
], required_vars) if value is None]

if missing_vars:
    raise EnvironmentError(f"⚠️ Missing environment variables: {', '.join(missing_vars)}")