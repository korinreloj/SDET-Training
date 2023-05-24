from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

PATH = "C:\\Users\\CorinneJoyceReloj\\PycharmProjects\\SDETTrainingProject\\driver\\chromedriver.exe"

#to open/launch chrome browser
driver = webdriver.Chrome(PATH)
url = "http://www.demo.guru99.com/test/drag_drop.html"
# url = "http://demo.guru99.com/test/simple_context_menu.html"

# open swaglab
driver.get(url)
driver.maximize_window()

action = ActionChains(driver)
# source_element1 = driver.find_element_by_xpath("//*[@id='credit2']")
# destination_element1 = driver.find_element_by_xpath("//ol[@id='bank']")
#
# action.drag_and_drop(source_element1, destination_element1)
# action.perform()
#
# source_element2 = driver.find_element_by_xpath("//*[@id='fourth'][1]")
# destination_element2 = driver.find_element_by_xpath("//ol[@id='amt7']")
#
# action.drag_and_drop(source_element2, destination_element2)
# action.perform()
#
# source_element3 = driver.find_element_by_xpath("//*[@id='credit1']")
# destination_element3 = driver.find_element_by_xpath("//ol[@id='loan']")
#
# action.drag_and_drop(source_element3, destination_element3)
# action.perform()
#
# source_element4 = driver.find_element_by_xpath("//*[@id='fourth'][1]")
# destination_element4 = driver.find_element_by_xpath("//ol[@id='amt8']")
#
# action.drag_and_drop(source_element4, destination_element4)
# action.perform()
#
# perfectButton = driver.find_element_by_xpath("//*[@id='equal']")
# assert perfectButton.is_displayed()
# print("Perfect Button is displayed")
# time.sleep(3)

# driver.quit()

#perform double click
# double_click_element = driver.find_element_by_xpath("//*[text()='Double-Click Me To See Alert']")
# action.double_click(double_click_element).perform()
# time.sleep(2)
#
# #handling the alert on the webpage
alert = Alert(driver)
# text = alert.text
# print(text)
# #alert.accept()
#
# alert.dismiss()
# time.sleep(10)

#perform right click operation
# right_click_element = driver.find_element_by_xpath("//*[text()='right click me']")
# action.context_click(right_click_element).perform()
# time.sleep(2)
#
# copy_option = driver.find_element_by_xpath("//*[text()='Copy']")
# copy_option.click()
# # action.move_to_element(copy_option).click().perform()
# time.sleep(3)
# alert.dismiss()
# time.sleep(3)


# perform hold and release action on the element
hold_element = driver.find_element_by_xpath("//*[@id='credit4']")
action.click_and_hold(hold_element).perform()
time.sleep(5)
action.release(hold_element).perform()

#perform keys operation via actions class in the webpage
# action = ActionChains(driver)
# action.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()
# print('You Pressed Highlight All!')
# time.sleep(2)

# perform mouse hover operation using actions class on a webelement
# nav_element = driver.find_element_by_xpath("//*[@id='navbar-brand-centered']/ul/li[1]/a")
# nav_element.click()
# time.sleep(2)
#
# copy_option = driver.find_element_by_xpath("//*[text()='Ajax Demo']")
# action.move_to_element(copy_option).click().perform()
# time.sleep(3)

driver.find

# driver.quit()