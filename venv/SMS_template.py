import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def generate_random_name():
    return ''.join(random.choices(string.ascii_lowercase, k=7))

def sms():
    random_username = generate_random_name()
    print("Generated name:", random_username)

    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Optional: start full screen

    # Initialize Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(10)

    # Step 1: Open the site
    driver.get("https://staging-v2.arworkflow.com/")

    # Step 2: Log in
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys("arunkumar.vadivel@mallow-tech.com")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Qazplm54321@")
    driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']").click()


    # SMS Template Create
    driver.find_element(By.XPATH, "//span[normalize-space()='Actions']").click()
    driver.find_element(By.XPATH, "//span[normalize-space()='SMS']").click()
    driver.find_element(By.XPATH, "//button[normalize-space()='Create Template']").click()
    template_name = driver.find_element(By.XPATH, "//input[@name='smsTemplate.templateName']")
    template_name.send_keys(random_username)
    Name=template_name.get_attribute("value") #Store the template name
    content = driver.find_element(By.XPATH, "//div[@role='textbox']")
    content.send_keys("hello this is a test message")
    merge_fields = driver.find_element(By.XPATH, "//button[@role='combobox']")
    merge_fields.click()
    time.sleep(5)
    actions = ActionChains(driver)
    #actions.send_keys(Keys.ARROW_DOWN)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    time.sleep(10)

    #verify the Created SMS in Search

    Searchbox=driver.find_element(By.XPATH,"//*[@placeholder='Search']")
    Searchbox.send_keys(Name)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(5)

    #verify the created SMS

    wait = WebDriverWait(driver, 20)
    list = wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@class='flex items-center justify-between gap-5 self-stretch']//h6)[1]")))
    if list:
        assert Name in list.text
        print(f"SMS template created successfully with name: {list.text}")
    else:
        print("SMS not found in the list")

    wait = WebDriverWait(driver, 10)
    

    time.sleep(10)  # Pause to see results
    driver.quit()

sms()
