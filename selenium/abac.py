from selenium import webdriver
import time

PATH = "/home/jan/code/python/selenium/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("http://www.au.edu/index.php/study-programs/undergraduate-programs/85-engineering-1/2267-department-of-computer-engineering-1.html#first-year")
print(driver.title)

tables = driver.find_elements_by_class_name("tab-content")
for table in tables:
    print(table.text)
    header = table.find_element_by_id_name("first-year")
    print(header.text)

time.sleep(2)
driver.quit()
