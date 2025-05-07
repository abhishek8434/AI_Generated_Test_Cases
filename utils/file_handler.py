import os

def save_test_script(filename, content):
    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(f"tests/generated/{filename}"), exist_ok=True)

        # Check if content is valid
        if not content:
            print(f"❌ No content to save for {filename}")
            return None

        # Write content to file
        with open(f"tests/generated/{filename}", "w", encoding="utf-8") as file:
            file.write(content)
        
        print(f"✅ Successfully saved test script to {filename}")
        return filename
    except Exception as e:
        print(f"❌ Error saving file {filename}: {e}")
        return None
