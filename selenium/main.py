from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = '/home/jan/code/python/selenium/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get('https://techwithtim.net')

link = driver.find_element_by_link_text("Game Development With Python")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Snake Tutorial"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    element.click()

    driver.back()
    driver.back()
    driver.back()
    driver.forward()
    driver.forward()
finally:
    time.sleep(2)
    driver.quit()
