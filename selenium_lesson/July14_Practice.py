import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

PATH = "C:\\Users\\CorinneJoyceReloj\\PycharmProjects\\SDETTrainingProject\\driver\\chromedriver.exe"

#to open/launch chrome browser
driver = webdriver.Chrome(PATH)
url = "http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Login.aspx?ReturnUrl=%2fsamples%2fTestComplete11%2fWebOrders%2fDefault.aspx"

driver.get(url)
driver.maximize_window()

userName = driver.find_element_by_xpath("//input[@name='ctl00$MainContent$username']")
userName.send_keys("Tester")
time.sleep(1)

password = driver.find_element_by_xpath("//input[@type='password']")
password.send_keys("test")
time.sleep(1)

submitButton = driver.find_element_by_xpath("//*[@value='Login']")
submitButton.click()
time.sleep(1)


order_tab = driver.find_element_by_xpath("//*[@id='ctl00_menu']/li[3]/a")
order_tab.click()
time.sleep(1)

product = Select(driver.find_element_by_xpath("//*[@id='ctl00_MainContent_fmwOrder_ddlProduct']"))
product.select_by_value("FamilyAlbum")
time.sleep(1)

quantity = driver.find_element_by_xpath("//*[@id='ctl00_MainContent_fmwOrder_txtQuantity']")
quantity.clear()
quantity.send_keys(10)
time.sleep(1)

calculate_button = driver.find_element_by_xpath("//*[@id='ctl00_MainContent_fmwOrder']/tbody/tr/td/ol[1]/li[5]/input[2]")
calculate_button.click()
time.sleep(1)

customerName = driver.find_element_by_xpath("//*[@id='ctl00_MainContent_fmwOrder_txtName']")
customerName.send_keys("Jaida Essence Hall")
time.sleep(1)

street = driver.find_element_by_xpath("//*[@id='ctl00_MainContent_fmwOrder_TextBox2']")
street.send_keys("123 Sesame Street")
time.sleep(1)

city = driver.find_element_by_xpath("//*[@id='ctl00_MainContent_fmwOrder_TextBox3']")
city.send_keys("NYC")
time.sleep(1)

state = driver.find_element_by_xpath("//*[@id='ctl00_MainContent_fmwOrder_TextBox4']")
state.send_keys("NY")
time.sleep(1)

zipcode = driver.find_element_by_xpath("//*[@id='ctl00_MainContent_fmwOrder_TextBox5']")
zipcode.send_keys("9290")
time.sleep(1)

mastercard_type = driver.find_element_by_css_selector("#ctl00_MainContent_fmwOrder_cardList_1")
mastercard_type.click()
time.sleep(1)

cardNumber = driver.find_element_by_xpath("//*[@id='ctl00_MainContent_fmwOrder_TextBox6']")
cardNumber.send_keys("123567890")
time.sleep(1)

cardExpiry = driver.find_element_by_xpath("//*[@id='ctl00_MainContent_fmwOrder_TextBox1']")
cardExpiry.send_keys("09/28")
time.sleep(1)

process_button = driver.find_element_by_xpath("//*[@id='ctl00_MainContent_fmwOrder_InsertButton']")
process_button.click()

successful_message = driver.find_element_by_xpath("//*[@id='ctl00_MainContent_fmwOrder']/tbody/tr/td/div/strong")
assert successful_message.is_displayed()
print(successful_message.text)
time.sleep(2)

allOrders_tab = driver.find_element_by_xpath("//*[@id='ctl00_menu']/li[1]/a")
allOrders_tab.click()
time.sleep(2)

#check if order is in the table
customerName_order = driver.find_element_by_xpath("//*[text()='Jaida Essence Hall']")
assert customerName_order.is_displayed()
print("Order added for: " + customerName_order.text)
time.sleep(2)

driver.quit()