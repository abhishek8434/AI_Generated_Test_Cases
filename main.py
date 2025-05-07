from jira.jira_client import fetch_issue
from ai.generator import generate_test_case
from utils.file_handler import save_test_script
from config.settings import BASE_URL
from azure_integration.pipeline import AzurePipeline
from azure_integration.azure_client import AzureClient

import re


def main():
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
    

# def main():
#     # Step 3: Sanitize summary to create a filename
#     def slugify(text):
#         return re.sub(r'\W+', '_', text.lower()).strip('_')

#     # Fetch work item details from Azure Boards using AzureClient
#     azure_client = AzureClient()
#     work_item_details = azure_client.fetch_azure_work_item()

#     if not work_item_details:
#         print("⚠️ Unable to fetch work item details. Exiting...")
#         return

#     # Extract title and description
#     summary = work_item_details.get("title", "No_Title_Found")
#     description = work_item_details.get("description", "No_Description_Found")

#     # Generate test case based on description using AzurePipeline
#     azure_pipeline = AzurePipeline()
#     test_case = azure_pipeline.generate_test_case(description, base_url=BASE_URL)

#     # Generate dynamic filenames
#     filename_txt = f"test_{slugify(summary)}.txt"
#     filename_py = f"test_{slugify(summary)}.py"

#     # Step 5: Save to dynamic filename
#     output1 = save_test_script(filename_txt, test_case)
#     output2 = save_test_script(filename_py, test_case)

#     print(f"✅ Test case saved as: {output1}")
#     print(f"✅ Test case saved as: {output2}")


if __name__ == "__main__":
    main()