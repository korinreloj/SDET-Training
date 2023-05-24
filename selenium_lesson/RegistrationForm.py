from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

PATH = "C:\\Users\\CorinneJoyceReloj\\PycharmProjects\\SDETTrainingProject\\driver\\chromedriver.exe"

#to open/launch chrome browser
driver = webdriver.Chrome(PATH)
url = "http://demo.guru99.com/test/newtours/"

#to open the app in browser
driver.get(url)

#to maximize window
driver.maximize_window()

#application url
print(driver.current_url)

#application title
print(driver.title)

username = driver.find_element_by_name("userName")
username.send_keys("test12345")
driver.implicitly_wait(1)
password = driver.find_element_by_name("password")
password.send_keys("test")
driver.implicitly_wait(1)

submitButton = driver.find_element_by_name("submit")
submitButton.click()
driver.implicitly_wait(4)

#quit closes your entire browser screen while close just closes your current window
driver.quit()
#driver.close()