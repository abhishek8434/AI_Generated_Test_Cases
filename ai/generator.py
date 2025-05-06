from openai import OpenAI
from config.settings import OPENAI_API_KEY, BASE_URL

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_test_case(description, base_url=BASE_URL):
    prompt = f"""
You are a senior QA engineer.

Your task is to generate **detailed Selenium Behave (BDD) test cases in Python** based on the requirement provided below. Use the given BASE URL for all tests.

**Mandatory Instruction**: You MUST include of:
- Positive test cases
- Negative test cases
- Edge test case
- Security test case
- Usability, Performance, or Compatibility test (if applicable)


Base URL: {base_url}

Requirement:
\"\"\"{description}\"\"\"

For each test case, include:
1. **Test Case Title**
2. **Type** (Positive / Negative / Edge / Out-of-the-box)
3. **Gherkin Feature Scenario** in `.feature` file format
4. **Step Definitions** (Python code using Selenium, with realistic waits and assertions)

Ensure clear formatting. Separate each test case with the following divider:
==============================
"""

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
        max_tokens=2000 #You can adjust based on expected response size
    )

    return response.choices[0].message.content.strip()
