from jira.jira_client import fetch_issue
from ai.generator import generate_test_case
from utils.file_handler import save_test_script
from config.settings import BASE_URL
import re

issue_key = "KAN-4"  # Replace with your Jira ticket
issue = fetch_issue(issue_key)
description = issue['fields']['description']
summary = issue['fields']['summary']

test_case = generate_test_case(description, base_url=BASE_URL)

# Save it as a Python test script
# save_test_script("test_reset_password.py", test_case)

# Step 3: Sanitize summary to create a filename
def slugify(text):
    return re.sub(r'\W+', '_', text.lower()).strip('_')

filename1 = f"test_{slugify(summary)}.txt"

filename2 = f"test_{slugify(summary)}.py"

# Step 4: Generate test case
test_case = generate_test_case(description, base_url=BASE_URL)

# Step 5: Save to dynamic filename
output1 = save_test_script(filename1, test_case)
output2 = save_test_script(filename2, test_case)

print(f"✅ Test case saved as: {filename1}")

print(f"✅ Test case saved as: {filename2}")