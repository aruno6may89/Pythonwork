import unittest
from selenium import webdriver
import HtmlTestRunner

class GoogleTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_google_title(self):
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
