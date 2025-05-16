
# AI Test Case Generator

This project automates the generation of detailed Selenium test cases in Python using OpenAI's GPT-4 model. It integrates with Jira, Azure DevOps, and image-based inputs to generate comprehensive test cases.

## Features

- Multi-platform integration:
  - Fetch Jira issue details using the Jira REST API
  - Fetch Azure DevOps work items using the Azure DevOps REST API
  - Generate test cases from UI/UX images or screenshots
- Generate detailed Selenium test cases, including:
  - Positive test cases
  - Negative test cases
  - Edge test cases
  - Security test cases
  - Usability, performance, or compatibility tests (if applicable)
- Save generated test cases as Python scripts or text files
- Dynamic filename generation based on issue/work item summary
- Template-based test case generation

## Project Structure

```tree
├── .env # Environment variables 
├── .gitignore # Git ignore file 
├── README.md # Project documentation
├── main.py # Main script to run the application 
├── requirements.txt # Python dependencies 
├── ai/ 
│   ├── generator.py # Test case generation logic using OpenAI
│   └── image_generator.py # Image-based test case generation 
├── azure_integration/
│   ├── __init__.py
│   ├── azure_client.py # Azure DevOps integration
│   └── pipeline.py # Pipeline configuration
├── config/ 
│   └── settings.py # Configuration settings (e.g., API keys, URLs) 
├── jira/ 
│   └── jira_client.py # Jira client to fetch issue details 
├── utils/ 
│   ├── file_handler.py # Utility to save test scripts 
│   └── logger.py # Logging utilities
├── tests/ 
│   ├── templates/ # Test case templates
│   └── generated/ # Directory for generated test cases
```


## Prerequisites

- Python 3.10 or higher

### Required Libraries

- **openai**: Integration with GPT-4 API for test case generation
- **requests**: HTTP client for Jira and Azure DevOps API integration
- **python-dotenv**: Environment variable management
- **beautifulsoup4**: HTML parsing for Azure work item descriptions
- **pandas**: Excel report generation and data handling
- **Pillow**: Image processing for image-based test case generation

### Built-in Libraries Used

- **typing**: Type hints for better code documentation
- **logging**: Application logging and error tracking
- **os**: Operating system interface for file and path operations
- **base64**: Encoding for Azure DevOps authentication
- **re**: Regular expressions for text processing

### Environment Variables Required

#### For OpenAI
- `OPENAI_API_KEY`: Your OpenAI API key

#### For Jira Integration
- `JIRA_URL`: Your Jira instance URL
- `JIRA_USER`: Jira username/email
- `JIRA_API_TOKEN`: Jira API token
- `JIRA_ISSUE_KEYS`: Comma-separated list of Jira issue keys (for batch processing)

#### For Azure DevOps Integration
- `AZURE_DEVOPS_URL`: Azure DevOps URL
- `AZURE_DEVOPS_ORG`: Your organization name
- `AZURE_DEVOPS_PROJECT`: Your project name
- `AZURE_DEVOPS_PAT`: Personal Access Token
- `AZURE_DEVOPS_WORKITEM_IDS`: Comma-separated list of work item IDs (for batch processing)
- `AZURE_DEVOPS_USER_STORY_ID`: User story ID (for processing all tasks under a user story)

#### General Settings
- `BASE_URL`: Base URL for test cases
- A virtual environment (recommended)
- Jira account with API access (for Jira integration)
- Azure DevOps account with API access (for Azure integration)
- OpenAI API key

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ai-testcase-generator
   ```

2. Create a virtual environment:
    ```bash
    python -m venv myenv
    source myenv/Scripts/activate  # On Windows
    source myenv/bin/activate      # On macOS/Linux
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a .env file in the root directory and add the following variables:
    ```bash
    # OpenAI Configuration
    OPENAI_API_KEY=<your_openai_api_key>

    # Jira Configuration
    JIRA_URL=<your_jira_url>
    JIRA_USER=<your_jira_username>
    JIRA_API_TOKEN=<your_jira_api_token>

    # Azure DevOps Configuration
    AZURE_DEVOPS_URL=<your_azure_devops_url>
    AZURE_DEVOPS_ORG=<your_organization_name>
    AZURE_DEVOPS_PROJECT=<your_project_name>
    AZURE_DEVOPS_PAT=<your_personal_access_token>
    AZURE_DEVOPS_WORKITEM_ID=<your_work_item_id>

    # Image Generation Configuration
    TEST_IMAGE_SOURCE=<path_to_image_file>
    TEST_IMAGE_TITLE=<your_image_title>

    # Application Configuration
    BASE_URL=<your_base_url>
    ```

## Usage

1. Update the issue_key in .env with your Jira ticket ID / Azure Workitem ID.
2. Run the main script:
    ```bash
    python main.py
    ```

The generated test cases will be saved in the tests/generated/ directory.

## Example Output
Generated test cases will include:

- Test case title
- Type (Positive/Negative/Edge/Security/Usability/Performance/Compatibility)
- Step-by-step actions
- Expected results
- Python Selenium test script
- Behave BDD feature files

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## Acknowledgments
- OpenAI for the GPT-4 model.
- Atlassian Jira for the Jira REST API.
- Microsoft Azure DevOps for the Work Items REST API.
