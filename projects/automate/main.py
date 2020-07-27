from selenium import webdriver

driver = webdriver.Firefox(executable_path='./geckodriver')
driver.get('https://youtube.com')
searchbox = driver.find_element_by_xpath('//input[@id="search"]')
print(searchbox)
searchbox.send_keys('Jan Poonthong')


searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
print(searchButton)
searchButton.click()
