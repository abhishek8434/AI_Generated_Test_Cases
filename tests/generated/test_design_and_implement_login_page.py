==============================
Test Case Title: Test Login with Valid Credentials
Type: Positive
Step-by-step Actions:
1. Open the browser and navigate to the base URL.
2. Enter a valid email/username and password.
3. Click on the login button.
Expected Result: The user is redirected to the dashboard.
Python Selenium Test Script:
```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://practice.expandtesting.com/login")
driver.find_element_by_name("username").send_keys("valid_username")
driver.find_element_by_name("password").send_keys("valid_password")
driver.find_element_by_name("login").click()
assert "dashboard" in driver.current_url
driver.quit()
```
==============================
Test Case Title: Test Login with Invalid Credentials
Type: Negative
Step-by-step Actions:
1. Open the browser and navigate to the base URL.
2. Enter an invalid email/username and password.
3. Click on the login button.
Expected Result: An error message is displayed indicating invalid credentials.
Python Selenium Test Script:
```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://practice.expandtesting.com/login")
driver.find_element_by_name("username").send_keys("invalid_username")
driver.find_element_by_name("password").send_keys("invalid_password")
driver.find_element_by_name("login").click()
assert "Invalid credentials" in driver.page_source
driver.quit()
```
==============================
Test Case Title: Test Login with Empty Credentials
Type: Negative
Step-by-step Actions:
1. Open the browser and navigate to the base URL.
2. Leave the email/username and password fields empty.
3. Click on the login button.
Expected Result: An error message is displayed indicating that the fields are required.
Python Selenium Test Script:
```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://practice.expandtesting.com/login")
driver.find_element_by_name("login").click()
assert "This field is required" in driver.page_source
driver.quit()
```
==============================
Test Case Title: Test Login with XSS Attack
Type: Security
Step-by-step Actions:
1. Open the browser and navigate to the base URL.
2. Enter a script in the email/username field (e.g., `<script>alert('XSS')</script>`).
3. Click on the login button.
Expected Result: The script is not executed and an error message is displayed indicating invalid input.
Python Selenium Test Script:
```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://practice.expandtesting.com/login")
driver.find_element_by_name("username").send_keys("<script>alert('XSS')</script>")
driver.find_element_by_name("login").click()
assert "<script>alert('XSS')</script>" not in driver.page_source
assert "Invalid input" in driver.page_source
driver.quit()
```
==============================
Test Case Title: Test Login Form Responsiveness
Type: Compatibility
Step-by-step Actions:
1. Open the browser and navigate to the base URL.
2. Resize the browser window to different sizes.
Expected Result: The login form adjusts its layout to fit the window size.
Python Selenium Test Script:
```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://practice.expandtesting.com/login")
sizes = [(800, 600), (1024, 768), (1280, 1024), (1366, 768), (1920, 1080)]
for size in sizes:
    driver.set_window_size(size[0], size[1])
    assert driver.find_element_by_name("login").is_displayed()
driver.quit()
```
==============================
