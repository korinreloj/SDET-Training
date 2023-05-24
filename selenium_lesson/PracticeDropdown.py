from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

PATH = "C:\\Users\\CorinneJoyceReloj\\PycharmProjects\\SDETTrainingProject\\driver\\chromedriver.exe"

#to open/launch chrome browser
driver = webdriver.Chrome(PATH)
url = "https://www.browserstack.com/"

driver.get(url)
driver.maximize_window()

dropdown = driver.find_element_by_xpath("//*[@id='developers-menu-toggle']")
dropdown.click()

selectDropdown = Select(driver.find_element_by_xpath("//ul[@id='developers-menu-dropdown']"))
selectDropdown.select_by_index(1)

driver.quit()