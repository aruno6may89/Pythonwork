import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Load Excel file
df = pd.read_excel('testdata.xlsx')  # make sure the file is in the same directory or provide full path

# Launch browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear
driver.get('https://staging-v2.arworkflow.com/')  # replace with your login page URL

# Loop through each row and use the data
for index, row in df.iterrows():
    username = row['Username']
    password = row['Password']

    # Find input fields and enter data
    Emailfield=driver.find_element(By.XPATH, "//input[@type='email']")
    Emailfield.send_keys(username)

    Passkey=driver.find_element(By.XPATH, "//input[@type='password']")
    Passkey.send_keys(password)

    # Submit or click login
    driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']").click()

    # Add any validation or logout step as needed
    print(f"Test run with username: {username} and password: {password}")
    

# Close the browser
driver.quit()
