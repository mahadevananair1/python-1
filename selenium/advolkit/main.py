from selenium import webdriver
import os.path

project_directory = os.path.dirname(__file__)
PATH = (os.path.join(project_directory, "../cookie/./chromedriver"))

driver = webdriver.Chrome(PATH)
driver.get("https://www.twitch.tv/advolkit")
