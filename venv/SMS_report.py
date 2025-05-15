import time
import random
import string
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def generate_random_name():
    return ''.join(random.choices(string.ascii_lowercase, k=7))

class TestSMSTemplate(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--headless")  # For CI/CD
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.implicitly_wait(10)
        self.actions = ActionChains(self.driver)

    def test_create_sms_template(self):
        driver = self.driver
        random_username = generate_random_name()
        print("Generated SMS template name:", random_username)

        # Step 1: Open the site and log in
        driver.get("https://staging-v2.arworkflow.com/")
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys("arunkumar.vadivel@mallow-tech.com")
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Qazplm54321@")
        driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']").click()

        # Step 2: Navigate to SMS Template and Create New
        driver.find_element(By.XPATH, "//span[normalize-space()='Actions']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='SMS']").click()
        driver.find_element(By.XPATH, "//button[normalize-space()='Create Template']").click()

        template_name = driver.find_element(By.XPATH, "//input[@name='smsTemplate.templateName']")
        template_name.send_keys(random_username)
        name_entered = template_name.get_attribute("value")

        content = driver.find_element(By.XPATH, "//div[@role='textbox']")
        content.send_keys("hello this is a test message")

        driver.find_element(By.XPATH, "//button[@role='combobox']").click()
        time.sleep(2)
        self.actions.send_keys(Keys.ENTER).perform()

        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)

        # Step 3: Search the created SMS
        search_box = driver.find_element(By.XPATH, "//*[@placeholder='Search']")
        search_box.send_keys(name_entered)
        self.actions.send_keys(Keys.ENTER).perform()
        time.sleep(3)

        # Step 4: Verify creation
        wait = WebDriverWait(driver, 20)
        sms_list_item = wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@class='flex items-center justify-between gap-5 self-stretch']//h6)[1]")))

        self.assertIn(name_entered, sms_list_item.text)
        print(f"✅ SMS template created successfully with name: {sms_list_item.text}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
