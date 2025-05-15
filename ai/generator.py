from openai import OpenAI
from config.settings import OPENAI_API_KEY, BASE_URL
from typing import Optional

# Initialize OpenAI client once at module level
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_test_case(description: str, base_url: str = BASE_URL) -> Optional[str]:
    """Generate detailed Selenium Behave (BDD) test cases based on the requirement.

    Args:
        description (str): The requirement description
        base_url (str): Base URL for the tests

    Returns:
        Optional[str]: Generated test cases or None if generation fails
    """
    if not description or not base_url:
        print("❌ Description or base_url cannot be empty")
        return None

    prompt = f"""
    You are a senior QA engineer.

    Your task is to generate **detailed Selenium Behave (BDD) test cases in Python** based on the requirement provided below. Use the given BASE URL for all tests.

    **Mandatory Instruction**: You MUST include:
    - Positive test cases
    - Negative test cases
    - Edge test case
    - Security test case
    - Usability, Performance, or Compatibility test (if applicable)

    Base URL: {base_url}

    Requirement:{description}

        For each test case, include:
        1. **Test Case Title**
        2. **Type** (Positive / Negative / Edge / Out-of-the-box)
        3. **Gherkin Feature Scenario** in `.feature` file format
        4. **Step Definitions** (Python code using Selenium, with realistic waits and assertions)

        Ensure clear formatting. Separate each test case with the following divider:
        ==============================
        """

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "You are a senior QA engineer generating Behave BDD test cases with Gherkin and Python Selenium."
                },
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=4000
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"❌ Error generating test case: {e}")
        return None
