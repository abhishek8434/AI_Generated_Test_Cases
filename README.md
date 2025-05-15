
# AI Test Case Generator

This project automates the generation of detailed Selenium test cases in Python using OpenAI's GPT-4 model. It integrates with both Jira and Azure DevOps to fetch work item details and generates comprehensive test cases based on the item description.

## Features

- Multi-platform integration:
  - Fetch Jira issue details using the Jira REST API
  - Fetch Azure DevOps work items using the Azure DevOps REST API
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
│   └── generator.py # Test case generation logic using OpenAI 
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
