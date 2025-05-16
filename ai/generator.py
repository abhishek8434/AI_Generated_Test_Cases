from openai import OpenAI
from config.settings import OPENAI_API_KEY
from typing import Optional, List

# Initialize OpenAI client once at module level
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_test_categories(task_title: str, task_description: str, category: str) -> Optional[str]:
    """Generate test cases for a specific category"""
    category_prompts = {
        "functional": """
        Generate Functional Test Cases including:
        - Positive test cases (happy path)
        - Negative test cases
        - Edge Cases test cases
        - Data validation cases
        """,
        "non_functional": """
        Generate Non-Functional Test Cases including:
        - Usability test cases
        - Compatibility test cases
        - Responsiveness test cases
        - UI test cases
        - UX test cases
        """
    }

    prompt = f"""
    You are a senior QA engineer.
    
    Task Title: {task_title}
    Task Description: {task_description}
    
    {category_prompts.get(category, "")}
    
    For each test case, use EXACTLY this format:
    
    Title: TC_MODULENAME_ID_Actual_Title
    Scenario: [Detailed scenario description]
    Steps to reproduce:
    1. [Step 1]
    2. [Step 2]
    ...
    Expected Result: [What should happen when test is successful]
    Actual Result: [To be filled after test execution]
    
    ==============================
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "You are a senior QA engineer generating detailed test cases."
                },
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=2000
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"❌ Error generating test cases for {category}: {e}")
        return None

def generate_test_case(task_title: str, task_description: str) -> Optional[str]:
    """Generate comprehensive test cases by breaking down into categories"""
    categories = ["functional", "non_functional"]
    all_test_cases = []

    for category in categories:
        test_cases = generate_test_categories(task_title, task_description, category)
        if test_cases:
            all_test_cases.append(test_cases)

    if not all_test_cases:
        return None

    return "\n\n".join(all_test_cases)


def generate_test_case(description: str, base_url: str = None) -> Optional[str]:
    """Generate detailed test cases based on the description.

    Args:
        description (str): The requirement description
        base_url (str, optional): Base URL for the tests if needed

    Returns:
        Optional[str]: Generated test cases or None if generation fails
    """
    if not description:
        print("❌ Description cannot be empty")
        return None

    # Convert description to string explicitly and split into chunks
    description_str = str(description)
    chunk_size = 2000
    description_chunks = []
    
    for i in range(0, len(description_str), chunk_size):
        chunk = description_str[i:i + chunk_size]
        description_chunks.append(chunk)
    
    all_test_cases = []
    test_types = [
        "Functional (positive, negative)",
        "Non-Functional (usability, compatibility, responsiveness, UI, UX)",
       
    ]

    for chunk_idx, desc_chunk in enumerate(description_chunks):
        chunk_prefix = f"Part {chunk_idx + 1}/{len(description_chunks)} of the requirement:\n"
        
        for test_type in test_types:
            prompt = f"""
            Generate {test_type} test cases for:
            {chunk_prefix}{desc_chunk}
            
            Format:
            Title: TC_MODULENAME_ID_Title
            Scenario: [Brief description]
            Steps to reproduce:
            1. [Step]
            2. [Step]
            Expected Result: [Outcome]
            Actual Result: [To be filled]
            
            ==============================
            """

            try:
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {
                            "role": "system",
                            "content": "QA engineer generating test cases."
                        },
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.3,
                    max_tokens=1000
                )
                result = response.choices[0].message.content.strip()
                if result:
                    all_test_cases.append(result)
            except Exception as e:
                print(f"❌ Error generating {test_type} test cases for chunk {chunk_idx + 1}: {e}")
                continue

    if not all_test_cases:
        return None

    return "\n\n".join(all_test_cases)
