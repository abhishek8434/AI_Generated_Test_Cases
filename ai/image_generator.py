from openai import OpenAI
from config.settings import OPENAI_API_KEY
from typing import Optional
import base64
import requests
import os

client = OpenAI(api_key=OPENAI_API_KEY)

def encode_image_from_url(image_url: str) -> Optional[str]:
    """Encode image from URL to base64."""
    try:
        response = requests.get(image_url)
        return base64.b64encode(response.content).decode('utf-8')
    except Exception as e:
        print(f"❌ Error encoding image from URL: {e}")
        return None

def encode_image_from_path(image_path: str) -> Optional[str]:
    """Encode image from local path to base64."""
    try:
        with open(image_path, 'rb') as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except Exception as e:
        print(f"❌ Error encoding image from path: {e}")
        return None

def generate_test_case_from_image(image_source: str, is_url: bool = False) -> Optional[str]:
    """Generate test cases from an image source (URL or local path).
    
    Args:
        image_source (str): URL or local path to the image
        is_url (bool): True if image_source is a URL, False if it's a local path
    
    Returns:
        Optional[str]: Generated test cases or None if generation fails
    """
    try:
        # Encode image based on source type
        base64_image = encode_image_from_url(image_source) if is_url else encode_image_from_path(image_source)
        
        if not base64_image:
            return None

        prompt = """
        Analyze this image and generate comprehensive test cases. Include:
        - Functional test cases (positive, negative, edge cases)
        - UI/UX test cases
        - Compatibility test cases
        - Accessibility test cases
        - Responsiveness test cases
        
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

        response = client.chat.completions.create(
            model="gpt-4o",  # Updated from gpt-4-vision-preview to gpt-4o
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}",
                                "detail": "high"  # Add detail parameter for better image understanding
                            }
                        }
                    ]
                }
            ],
            max_tokens=2000
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"❌ Error generating test cases from image: {e}")
        return None