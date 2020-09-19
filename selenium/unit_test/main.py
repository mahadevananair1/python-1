import unittest
from selenium import webdriver
import page

class PythonOrgSearchTest(unittest.TestCase):

    def setUp(self):
        print("setup")
        self.driver = webdriver.Chrome("/home/jan/code/python/selenium/chromedriver")
        self.driver.get("http://www.python.org")

    def test_example(self):
        assert False

    def test_example_2(self):
        assert True

    def not_a_test(self):
        print("Not a test")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
