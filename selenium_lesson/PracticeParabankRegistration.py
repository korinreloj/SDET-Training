from selenium import webdriver

PATH = "C:\\Users\\CorinneJoyceReloj\\PycharmProjects\\SDETTrainingProject\\driver\\chromedriver.exe"

#to open/launch chrome browser
driver = webdriver.Chrome(PATH)
url = "https://parabank.parasoft.com/parabank/index.htm"
driver.get(url)
driver.maximize_window()

registerLink = driver.find_element_by_xpath("//*[@id='loginPanel']/p[2]/a")
registerLink.click()
driver.implicitly_wait(3)

firstName = driver.find_element_by_xpath("//*[@class='form2']/tbody/tr[1]/td[2]/input")
firstName.send_keys("Brook Lynn")
driver.implicitly_wait(2)

lastName = driver.find_element_by_xpath("//*[@class='form2']/tbody/tr[2]/td[2]/input")
lastName.send_keys("Hytes")
driver.implicitly_wait(2)

address = driver.find_element_by_xpath("//*[@class='form2']/tbody/tr[3]/td[2]/input")
address.send_keys("123 Sesame Street")
driver.implicitly_wait(2)

city = driver.find_element_by_xpath("//*[@class='form2']/tbody/tr[4]/td[2]/input")
city.send_keys("NYC")
driver.implicitly_wait(2)

state = driver.find_element_by_xpath("//*[@class='form2']/tbody/tr[5]/td[2]/input")
state.send_keys("New York")
driver.implicitly_wait(2)

zipCode = driver.find_element_by_xpath("//*[@class='form2']/tbody/tr[6]/td[2]/input")
zipCode.send_keys("9000")
driver.implicitly_wait(2)

phoneNumber = driver.find_element_by_xpath("//*[@class='form2']/tbody/tr[7]/td[2]/input")
phoneNumber.send_keys("1234567")
driver.implicitly_wait(2)

ssn = driver.find_element_by_xpath("//*[@class='form2']/tbody/tr[8]/td[2]/input")
ssn.send_keys("0000044357667")
driver.implicitly_wait(2)

userName = driver.find_element_by_xpath("//*[@class='form2']/tbody/tr[10]/td[2]/input")
userName.send_keys("brooklynnHytes")
driver.implicitly_wait(2)

password = driver.find_element_by_xpath("//*[@class='form2']/tbody/tr[11]/td[2]/input")
password.send_keys("brooklynnHytes123")
driver.implicitly_wait(2)

confirmPassword = driver.find_element_by_xpath("//*[@class='form2']/tbody/tr[12]/td[2]/input")
confirmPassword.send_keys("brooklynnHytes123")
driver.implicitly_wait(2)

submitButton = driver.find_element_by_xpath("//*[@class='form2']/tbody/tr[13]/td[2]/input")
submitButton.click()
driver.implicitly_wait(5)

driver.quit()