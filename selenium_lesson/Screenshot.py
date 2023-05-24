from selenium import webdriver
import time
from PIL import Image


PATH = "C:\\Users\\CorinneJoyceReloj\\PycharmProjects\\SDETTrainingProject\\driver\\chromedriver.exe"

#to open/launch chrome browser
driver = webdriver.Chrome(PATH)
url = "http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Login.aspx?ReturnUrl=%2fsamples%2fTestComplete11%2fWebOrders%2fDefault.aspx"

#open url
driver.get(url)

#maximize window
driver.maximize_window()

loginTitle = "Web Orders Login"
assert loginTitle == driver.title

userName = driver.find_element_by_xpath("//input[@name='ctl00$MainContent$username']")
userName.send_keys("Tester")
driver.implicitly_wait(2)

#save the screenshot
driver.save_screenshot("image.png")
#loading the screenshot
image = Image.open("image.png")
#show the screenshot
image.show()