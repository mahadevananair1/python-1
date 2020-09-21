import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        print("setup")
        self.driver = webdriver.Chrome("/home/jan/code/python/selenium/chromedriver")
        self.driver.get("http://www.python.org")

    def test_1(self):
        print("Test")
        assert False

    def test_2(self):
        assert True

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
