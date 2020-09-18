from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = '/home/jan/code/python/selenium/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get('https://techwithtim.net')
print(driver.title)

search_bar = driver.find_element_by_name("s")
search_bar.send_keys("Django")
search_bar.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)
finally:
    driver.quit()
