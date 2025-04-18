from ssl import Options
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random
import string



# Function to generate a random username
def generate_random_name():
    return ''.join(random.choices(string.ascii_lowercase, k=7))

# Main test
def test_login():
    # Generate and store random username
    random_username = generate_random_name()
    print("Generated name:", random_username)

    # Set up WebDriver with implicit wait
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear

    # Step 1: Open the site Ar workflow
    driver.get("https://staging-v2.arworkflow.com/")
    
    # Step 2: Log in
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys("arunkumar.vadivel@mallow-tech.com")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Qazplm54321@")
    driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']").click()

    # Step 3: Navigate to Customers
    driver.find_element(By.XPATH, "//span[normalize-space()='Customers']").click()

    # Step 4: Click Add Customer
    driver.find_element(By.XPATH, "//*[normalize-space()='Add Customer']").click()

    # Step 5: Set the elaements into variables
    First_name=driver.find_element(By.XPATH, "//input[@name='firstName']")
    Middele_name=driver.find_element(By.XPATH, "//input[@name='middleName']")
    Last_name=driver.find_element(By.XPATH,"//input[@name='lastName']")

    #step 6 : enter the values into fields

    First_name.send_keys(random_username)
    Middele_name.send_keys(random_username)
    Last_name.send_keys("testone")

    #assertions
    label=driver.find_element(By.XPATH,"//label[normalize-space()='Company Name']")
    assert label.is_displayed()
    time.sleep(10)    # Done
    print("Successfully logged in and created customer with name:", random_username)
    driver.quit()

if __name__ == "__main__":
    test_login()
    