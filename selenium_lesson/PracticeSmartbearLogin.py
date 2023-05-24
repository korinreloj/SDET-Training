from selenium import webdriver

PATH = "C:\\Users\\CorinneJoyceReloj\\PycharmProjects\\SDETTrainingProject\\driver\\chromedriver.exe"

#to open/launch chrome browser
driver = webdriver.Chrome(PATH)
url = "http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Login.aspx?ReturnUrl=%2fsamples%2fTestComplete11%2fWebOrders%2fDefault.aspx"

driver.get(url)
driver.maximize_window()

loginTitle = "Web Orders Login"
assert loginTitle == driver.title

userName = driver.find_element_by_xpath("//input[@name='ctl00$MainContent$username']")
userName.send_keys("Tester")
driver.implicitly_wait(2)

password = driver.find_element_by_xpath("//input[@type='password']")
password.send_keys("test")
driver.implicitly_wait(2)

submitButton = driver.find_element_by_xpath("//*[@value='Login']")
submitButton.click()
driver.implicitly_wait(3)

homepageTitle = "Web Orders"
assert homepageTitle == driver.title

logoutButton = driver.find_element_by_xpath("//*[@id='ctl00_logout']")
logoutButton.click()
driver.implicitly_wait(5)

driver.quit()