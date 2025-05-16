#  
from jira.jira_client import fetch_issue
from ai.generator import generate_test_case
from utils.file_handler import save_test_script, save_excel_report
from config.settings import BASE_URL
from azure_integration.pipeline import AzurePipeline
from azure_integration.azure_client import AzureClient
from ai.image_generator import generate_test_case_from_image

import re
import os

    
"""For jira integration"""
def process_single_issue(issue_key):
    try:
        # Fetch issue details
        issue = fetch_issue(issue_key)
        description = issue['fields']['description']
        summary = issue['fields']['summary']

        def slugify(text):
            return re.sub(r'\W+', '_', text.lower()).strip('_')

        # Create unique filenames for this issue
        base_filename = f"test_{issue_key}_{slugify(summary)}"
        excel_filename = f"{base_filename}.xlsx"
        txt_filename = f"{base_filename}.txt"

        # Generate test cases
        test_case = generate_test_case(description)

        if test_case:
            # Save in both formats
            save_test_script(txt_filename, test_case)
            save_excel_report(excel_filename, test_case)
            print(f"✅ Test cases for {issue_key} saved as:\n   - {txt_filename}\n   - {excel_filename}")
            return True
        else:
            print(f"❌ Failed to generate test cases for {issue_key}")
            return False
    except Exception as e:
        print(f"❌ Error processing {issue_key}: {e}")
        return False
    
def main():
    # Get all issue keys from environment variable
    issue_keys = os.getenv('JIRA_ISSUE_KEYS', '').split(',')
    issue_keys = [key.strip() for key in issue_keys if key.strip()]

    if not issue_keys:
        print("❌ No issue keys provided. Set JIRA_ISSUE_KEYS environment variable")
        return

    print(f"🔄 Processing {len(issue_keys)} issues...\n")

    # Process each issue
    results = {
        'success': [],
        'failed': []
    }

    for issue_key in issue_keys:
        print(f"\n📋 Processing issue: {issue_key}")
        if process_single_issue(issue_key):
            results['success'].append(issue_key)
        else:
            results['failed'].append(issue_key)

    # Print summary
    print("\n📊 Summary:")
    print(f"✅ Successfully generated: {len(results['success'])} issues")
    print(f"❌ Failed: {len(results['failed'])} issues")

    if results['failed']:
        print("\n❌ Failed issues:")
        for issue in results['failed']:
            print(f"   - {issue}")

if __name__ == "__main__":
    main()
    
    
    
"""For azure integration"""
# def process_single_azure_item(work_item):
#     try:
#         description = work_item["description"]
#         summary = work_item["title"]
#         work_item_id = work_item["id"]

#         def slugify(text):
#             return re.sub(r'\W+', '_', text.lower()).strip('_')

#         # Create unique filenames for this work item
#         base_filename = f"test_azure_{work_item_id}_{slugify(summary)}"
#         excel_filename = f"{base_filename}.xlsx"
#         txt_filename = f"{base_filename}.txt"

#         # Generate test cases using AzurePipeline
#         azure_pipeline = AzurePipeline()
#         test_case = azure_pipeline.generate_test_case(description, base_url=BASE_URL)

#         if test_case:
#             # Save in both formats
#             save_test_script(txt_filename, test_case)
#             save_excel_report(excel_filename, test_case)
#             print(f"✅ Test cases for work item {work_item_id} saved as:\n   - {txt_filename}\n   - {excel_filename}")
#             return True
#         else:
#             print(f"❌ Failed to generate test cases for work item {work_item_id}")
#             return False
#     except Exception as e:
#         print(f"❌ Error processing work item {work_item_id}: {e}")
#         return False

# def main():
#     # Initialize Azure client
#     azure_client = AzureClient()
    
#     # Fetch all work items
#     work_items = azure_client.fetch_azure_work_items()
    
#     if not work_items:
#         print("⚠️ No work items found or unable to fetch work items. Exiting...")
#         return

#     print(f"🔄 Processing {len(work_items)} work items...\n")

#     # Process each work item
#     results = {
#         'success': [],
#         'failed': []
#     }

#     for work_item in work_items:
#         work_item_id = work_item['id']
#         print(f"\n📋 Processing work item: {work_item_id}")
#         if process_single_azure_item(work_item):
#             results['success'].append(work_item_id)
#         else:
#             results['failed'].append(work_item_id)

#     # Print summary
#     print("\n📊 Summary:")
#     print(f"✅ Successfully generated: {len(results['success'])} work items")
#     print(f"❌ Failed: {len(results['failed'])} work items")

#     if results['failed']:
#         print("\n❌ Failed work items:")
#         for item in results['failed']:
#             print(f"   - {item}")

# if __name__ == "__main__":
#     main()
    
    
"""For image integration"""

# def process_image_test_case(image_source, is_url=False, title="UI_Test"):
#     """Generate test cases from an image source.
    
#     Args:
#         image_source (str): URL or path to the image
#         is_url (bool): True if image_source is a URL, False if local path
#         title (str): Title for the test case files
    
#     Returns:
#         bool: True if successful, False otherwise
#     """
#     try:
#         def slugify(text):
#             return re.sub(r'\W+', '_', text.lower()).strip('_')

#         # Create unique filenames
#         base_filename = f"test_image_{slugify(title)}"
#         excel_filename = f"{base_filename}.xlsx"
#         txt_filename = f"{base_filename}.txt"

#         # Generate test cases from image
#         test_case = generate_test_case_from_image(image_source, is_url)

#         if test_case:
#             # Save in both formats
#             save_test_script(txt_filename, test_case)
#             save_excel_report(excel_filename, test_case)
#             print(f"✅ Image-based test cases saved as:\n   - {txt_filename}\n   - {excel_filename}")
#             return True
#         else:
#             print(f"❌ Failed to generate test cases from image")
#             return False
#     except Exception as e:
#         print(f"❌ Error processing image test case: {e}")
#         return False

# # Comment out this section when not using image-based test generation
# def main_image():
#     """Main function for image-based test case generation.
#     Comment out this entire function when not needed.
#     """
#     print("🔄 Starting image-based test case generation...\n")

#     # Get image source from environment variable
#     image_source = os.getenv('TEST_IMAGE_SOURCE')
#     if not image_source:
#         print("❌ No image source provided. Set TEST_IMAGE_SOURCE environment variable")
#         return

#     # Determine if it's a URL or local path
#     is_url = image_source.lower().startswith(('http://', 'https://'))
    
#     # Get optional title
#     title = os.getenv('TEST_IMAGE_TITLE', 'UI_Test')

#     # Process multiple images if comma-separated
#     image_sources = image_source.split(',')
#     titles = title.split(',') if ',' in title else [title] * len(image_sources)

#     results = {
#         'success': [],
#         'failed': []
#     }

#     for img_src, img_title in zip(image_sources, titles):
#         img_src = img_src.strip()
#         img_title = img_title.strip()
        
#         print(f"\n📋 Processing image: {img_title}")
#         if process_image_test_case(img_src, is_url, img_title):
#             results['success'].append(img_title)
#         else:
#             results['failed'].append(img_title)

#     # Print summary
#     print("\n📊 Summary:")
#     print(f"✅ Successfully generated: {len(results['success'])} test cases")
#     print(f"❌ Failed: {len(results['failed'])} test cases")

#     if results['failed']:
#         print("\n❌ Failed test cases:")
#         for title in results['failed']:
#             print(f"   - {title}")

# # Comment/uncomment the appropriate main function call
# if __name__ == "__main__":
#     main_image()  # For image-based test generation
