import time

from selenium import webdriver

PATH = "/driver/chromedriver.exe"

#to open/launch chrome browser
driver = webdriver.Chrome(PATH)
url = "http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Login.aspx?ReturnUrl=%2fsamples%2fTestComplete11%2fWebOrders%2fDefault.aspx"

driver.get(url)
driver.maximize_window()

username = driver.find_element_by_css_selector("input#ctl00_MainContent_username")
password = driver.find_element_by_xpath("//input[@type='password']")
loginButton = driver.find_element_by_xpath("//*[@value='Login']")

if username.is_displayed():
    username.send_keys("Timmy")
    time.sleep(2)
    username.clear()
    username.send_keys("Tester")

if password.is_displayed():
    password.send_keys("Timmy")
    time.sleep(2)
    password.clear()
    password.send_keys("test")

if loginButton.is_displayed():
    loginButton.click()
    time.sleep(2)

#verification of my homepage title
title = "Web Orders"
expectedTitle = driver.title

if title == expectedTitle:
    print("My test case is passed")
else:
    print("My test case is failed")

heading_title = driver.find_element_by_xpath("//div[@class='content']/h2")
#expectedHeading = "List of All Orders"

if heading_title.is_displayed():
    heading = heading_title.text
    print(heading)

#assert heading_title == expectedHeading
#print("Passed:::::::")

currentPage = driver.find_element_by_css_selector("li.selected")
expectedCurrentPage = "View all orders"
assert currentPage.is_displayed()
assert currentPage.text == expectedCurrentPage
print("Passed:::::::")

logoutButton = driver.find_element_by_css_selector("a#ctl00_logout")

if logoutButton.is_displayed():
    logoutButton.click()
    time.sleep(2)

driver.quit()