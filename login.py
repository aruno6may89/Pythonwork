from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to the login page
driver.get("https://example.com/login")  # Replace with your actual login URL

# Maximize the window (optional)
driver.maximize_window()

# Enter username
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("your_username")  # Replace with your actual username

# Enter password
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("your_password")  # Replace with your actual password

# Click login button
login_button = driver.find_element(By.ID, "loginBtn")
login_button.click()

# Wait for a while to let page load after login
time.sleep(5)

# Optional: Check if login is successful
print("Page title after login:", driver.title)

# Quit the browser
driver.quit()
