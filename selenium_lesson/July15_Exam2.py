import time
from selenium import webdriver

PATH = "C:\\Users\\CorinneJoyceReloj\\PycharmProjects\\SDETTrainingProject\\driver\\chromedriver.exe"

#to open/launch chrome browser
driver = webdriver.Chrome(PATH)
url = "http://hrm.syntaxtechs.net/humanresources/symfony/web/index.php/auth/login"

driver.get(url)
driver.maximize_window()

invalid_username = "abc123"
invalid_password = "abCDE123"

#login page
username_input = driver.find_element_by_xpath("//*[@id='txtUsername']")
username_input.send_keys(invalid_username)
time.sleep(1)

password_input = driver.find_element_by_xpath("//*[@id='txtPassword']")
password_input.send_keys(invalid_password)
time.sleep(1)

login_button = driver.find_element_by_xpath("//*[@id='btnLogin']")
login_button.click()
time.sleep(1)

error = driver.find_element_by_xpath("//*[text()='Invalid credentials']")
assert error.is_displayed()
error_message = error.text
print("Passed:::Error Message: " + error_message)
time.sleep(1)

driver.quit()
