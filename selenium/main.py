from selenium import webdriver

PATH = '/home/jan/code/python/selenium/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get('https://youtube.com')