from openai import OpenAI
from config.settings import OPENAI_API_KEY, BASE_URL

client = OpenAI(api_key=OPENAI_API_KEY)

class AzurePipeline:
    def generate_test_case(self, description, base_url=None):
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

        all_test_cases = []
        
        for category, category_prompt in category_prompts.items():
            prompt = f"""
            You are a senior QA engineer.
            
            Task Description: {description}
            
            {category_prompt}
            
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
                test_cases = response.choices[0].message.content.strip()
                if test_cases:
                    all_test_cases.append(test_cases)
            except Exception as e:
                print(f"❌ Error generating test cases for {category}: {e}")

        if not all_test_cases:
            return None

        return "\n\n".join(all_test_cases)
