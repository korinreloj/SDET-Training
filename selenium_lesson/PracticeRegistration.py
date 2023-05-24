#write script to automate starting 8 fields and send data there
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

PATH = "C:\\Users\\CorinneJoyceReloj\\PycharmProjects\\SDETTrainingProject\\driver\\chromedriver.exe"

#to open/launch chrome browser
driver = webdriver.Chrome(PATH)
url = "http://demo.guru99.com/test/newtours/register.php"

driver.get(url)

firstName = driver.find_element_by_name("firstName")
firstName.send_keys("Juan")
driver.implicitly_wait(2)

lastName = driver.find_element_by_name("lastName")
lastName.send_keys("Dela Cruz")
driver.implicitly_wait(2)

phone = driver.find_element_by_name("phone")
phone.send_keys("1234567890")
driver.implicitly_wait(2)

userName = driver.find_element_by_name("userName")
userName.send_keys("juan23")
driver.implicitly_wait(2)

address1 = driver.find_element_by_name("address1")
address1.send_keys("009 Sesame St.")
driver.implicitly_wait(2)

city = driver.find_element_by_name("city")
city.send_keys("NYC")
driver.implicitly_wait(2)

state = driver.find_element_by_name("state")
state.send_keys("NY")
driver.implicitly_wait(2)

postalCode = driver.find_element_by_name("postalCode")
postalCode.send_keys("1200")
driver.implicitly_wait(2)

#to automate dropdown values
selectCountry = Select(driver.find_element_by_name("country"))
#by value
selectCountry.select_by_value("UNITED STATES")
#by index starts at 0
selectCountry.select_by_index(32)
driver.implicitly_wait(2)

email = driver.find_element_by_name("email")
email.send_keys("Juan23")
driver.implicitly_wait(2)

password = driver.find_element_by_name("password")
password.send_keys("juan23!!!")
driver.implicitly_wait(2)

confirmPassword = driver.find_element_by_name("confirmPassword")
confirmPassword.send_keys("juan23!!!")
driver.implicitly_wait(2)

submitButton = driver.find_element_by_name("submit")
submitButton.click()
#driver.implicitly_wait(5)
time.sleep(3)
driver.quit()