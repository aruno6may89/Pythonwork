import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import time
import HtmlTestRunner

class SignInPageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.get("https://staging-v2.arworkflow.com/")
        cls.driver.maximize_window()
        cls.driver.delete_all_cookies()
        cls.driver.implicitly_wait(10)
        cls.random_text = cls.generate_random_string(10)

    @staticmethod
    def generate_random_string(length):
        characters = string.ascii_letters
        return ''.join(random.choice(characters) for _ in range(length))

    def test_1_login(self):
        self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys("arunkumar.vadivel@mallow-tech.com")
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Qazplm54321@")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']").click()

    def test_2_open_customer_creation_popup(self):
        self.click("//span[normalize-space()='Customers']")
        self.click("//button[normalize-space()='Add Customer']")

        expected_title = "Create Customer"
        actual_title = self.driver.find_element(By.XPATH, "//h6[normalize-space()='Create Customer']").text
        self.assertEqual(actual_title, expected_title, "This is not the Create Customer pop-up")

    def test_3_create_customer(self):
        # Name section
        self.send_text("//input[@placeholder='Enter Title']", self.random_text)
        self.send_text("//input[@placeholder='Enter First Name']", self.random_text)
        self.send_text("//input[@placeholder='Enter Middle Name']", self.random_text)
        self.send_text("//input[@placeholder='Enter Last Name']", self.random_text)
        self.send_text("//input[@placeholder='Enter Company Name']", self.random_text)

        # Contact section
        self.click("//button[normalize-space()='Contacts']")
        self.send_text("//input[@placeholder='Enter Email']", "ragul.subramani+1@mallow-tech.com")
        self.send_text("//input[@placeholder='Enter Mobile Number']", "9876543210")

        # Display Name
        self.click("//button[normalize-space()='Display Name']")
        self.send_text("//input[@placeholder='Enter Display Name']", "Tester")
        self.click("(//div[contains(@class, 'text-base') and contains(@class, 'font-normal')])[1]")

        # Address section
        self.click("//button[normalize-space()='Address']")
        self.send_text("//input[@name='billingAddress.line1']", self.random_text)
        self.send_text("//input[@name='billingAddress.line2']", self.random_text)
        self.send_text("//input[@name='billingAddress.city']", self.random_text)
        self.send_text("//input[@name='billingAddress.state']", self.random_text)
        self.send_text("//input[@name='billingAddress.postalCode']", self.random_text)
        self.click("//button[@id='sameAsBillingAddress']")

        

        # Customer ID section
        self.click("//button[normalize-space()='Customer ID']")
        self.send_text("//input[@placeholder='Enter ID Number']", self.random_text)

        # Save
        self.click("//button[normalize-space()='Save Changes']")
        time.sleep(10)

    def test_4_verify_customer(self):
        wait = WebDriverWait(self.driver, 10)

        # Open and apply filter
        filter_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div/div/div[2]/div[2]/div[1]/div[2]/div/button")))
        filter_btn.click()

        checkbox = wait.until(EC.element_to_be_clickable((By.ID, "statuses-inactive")))
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.click("//button[normalize-space()='Apply']")

        # Search
        self.send_text("//input[@placeholder='Search']", self.random_text)
        print("Customer Name:", self.random_text)

        # Verify
        time.sleep(20)
        actual_name = self.driver.find_element(By.XPATH, "//h6[contains(@class,'font-inter')]").text
        self.assertEqual(actual_name, self.random_text, "Customer name does not match.")

    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()

# Utility methods
    def click(self, xpath):
        self.driver.find_element(By.XPATH, xpath).click()

    def send_text(self, xpath, text):
        self.driver.find_element(By.XPATH, xpath).send_keys(text)

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
