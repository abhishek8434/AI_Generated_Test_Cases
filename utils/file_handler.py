import os
from typing import Optional
import logging
import pandas as pd

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
        
        # print(f"✅ Successfully saved test script to {filename}")
        return filename
    except Exception as e:
        print(f"❌ Error saving file {filename}: {e}")
        return None


def save_excel_report(filename: str, test_cases: str) -> Optional[str]:
    """Save test cases to Excel file.

    Args:
        filename (str): Name of the Excel file to save
        test_cases (str): Test cases content to write to Excel

    Returns:
        Optional[str]: Filename if successful, None otherwise
    """
    if not filename or not test_cases:
        print("❌ Filename and test cases cannot be empty")
        return None

    # Ensure filename has .xlsx extension
    if not filename.endswith('.xlsx'):
        filename = f"{filename}.xlsx"

    output_dir = os.path.join("tests", "generated")
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)

    try:
        # Parse test cases into structured data
        test_data = []
        current_test = {}
        for line in test_cases.split('\n'):
            line = line.strip()
            if line.startswith('Title:'):
                if current_test:
                    test_data.append(current_test)
                current_test = {'Title': line[6:].strip()}
            elif line.startswith('Scenario:'):
                current_test['Scenario'] = line[9:].strip()
            elif line.startswith('Steps to reproduce:'):
                current_test['Steps'] = []
            elif line.startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.')) and 'Steps' in current_test:
                current_test['Steps'].append(line.strip())
            elif line.startswith('Expected Result:'):
                current_test['Expected Result'] = line[16:].strip()
            elif line.startswith('Actual Result:'):
                current_test['Actual Result'] = line[14:].strip()

        if current_test:
            test_data.append(current_test)

        # Convert to DataFrame
        df = pd.DataFrame(test_data)
        
        # Convert steps list to string
        if 'Steps' in df.columns:
            df['Steps'] = df['Steps'].apply(lambda x: '\n'.join(x) if isinstance(x, list) else x)

        # Save to Excel
        df.to_excel(filepath, index=False, sheet_name='Test Cases')
        # print(f"✅ Excel report saved as: {filename}")
        return filename

    except Exception as e:
        print(f"❌ Error saving Excel report: {e}")
        return None
