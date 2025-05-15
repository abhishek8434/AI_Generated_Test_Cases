import os
from typing import Optional
import logging
def save_test_script(filename: str, content: str) -> Optional[str]:
    """Save test script to file.

    Args:
        filename (str): Name of the file to save
        content (str): Content to write to file

    Returns:
        Optional[str]: Filename if successful, None otherwise
    """
    if not filename or not content:
        print("❌ Filename and content cannot be empty")
        return None

    output_dir = os.path.join("tests", "generated")
    file_path = os.path.join(output_dir, filename)

    try:
        os.makedirs(output_dir, exist_ok=True)
        
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
        
        print(f"✅ Successfully saved test script to {filename}")
        return filename
    except Exception as e:
        print(f"❌ Error saving file {filename}: {e}")
        return None
