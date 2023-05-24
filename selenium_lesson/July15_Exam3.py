import time
from selenium import webdriver

PATH = "C:\\Users\\CorinneJoyceReloj\\PycharmProjects\\SDETTrainingProject\\driver\\chromedriver.exe"

#to open/launch chrome browser
driver = webdriver.Chrome(PATH)
url = "http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Default.aspx"

driver.get(url)
driver.maximize_window()

valid_username = "Tester"
valid_password = "test"

#login page
userName = driver.find_element_by_xpath("//input[@name='ctl00$MainContent$username']")
userName.send_keys(valid_username)
time.sleep(1)

password = driver.find_element_by_xpath("//input[@type='password']")
password.send_keys(valid_password)
time.sleep(1)

submitButton = driver.find_element_by_xpath("//*[@value='Login']")
submitButton.click()
time.sleep(1)

#home page
all_products_tab = driver.find_element_by_xpath("//*[@id='ctl00_menu']/li[2]/a")
all_products_tab.click()

#products page
products = ["MyMoney", "FamilyAlbum", "ScreenSaver"]

product1 = driver.find_element_by_xpath("//*[@id='aspnetForm']/table/tbody/tr/td[2]/div[2]/table/tbody/tr[2]/td[1]").text
assert product1 in products
print("Passed:::Product1 is in Products List: " + product1)

product2 = driver.find_element_by_xpath("//*[@id='aspnetForm']/table/tbody/tr/td[2]/div[2]/table/tbody/tr[3]/td[1]").text
assert product2 in products
print("Passed:::Product2 is in Products List: " + product2)

product3 = driver.find_element_by_xpath("//*[@id='aspnetForm']/table/tbody/tr/td[2]/div[2]/table/tbody/tr[4]/td[1]").text
assert product3 in products
print("Passed:::Product3 is in Products List: " + product3)

time.sleep(2)
driver.quit()