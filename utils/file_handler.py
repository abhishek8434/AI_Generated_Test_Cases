def save_test_script(filename, content):
    with open(f"tests/generated/{filename}", "w", encoding="utf-8") as f:
        f.write(content)
