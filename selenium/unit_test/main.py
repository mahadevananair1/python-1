import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/home/jan/code/python/selenium/chromedriver")
        self.driver.get("http://www.python.org")

    def test(self):
        print("Test")
        assert True

    def not_test(self):
        print("Not Test")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
