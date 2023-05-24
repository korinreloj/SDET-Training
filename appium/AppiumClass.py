from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

#app path -
#device id - 5554
#app package -.LoginActivity
# app activity -com.experitest.ExperiBank
#platform name -

app = "C:\\Users\\CorinneJoyceReloj\\Documents\\BPI PROJECT\\TESTING\\SDET TRAINING\\Mobile Automation Testing\\EriBank.apk"
print(app)

desired_caps = {
    'deviceName': 'Android Device',
    'deviceId': '5554',
    'platformName': 'Android',
    'appPackage': 'com.experitest.ExperiBank',
    'appActivity': '.LoginActivity',
    'app': app
}

print(desired_caps)
#default appium server: 127.0.0.1
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
print("Application launched successfully")

usernamefield = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((MobileBy.XPATH, "//*[@text='Username']")))
usernamefield.click()
usernamefield.send_keys("company")

passwordfield = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((MobileBy.XPATH, "//*[@text='Password']")))
passwordfield.click()
passwordfield.send_keys("company")

loginbutton = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((MobileBy.XPATH, "//*[@text='Login']")))
loginbutton.click()

makepaymentbutton = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((MobileBy.XPATH, "//*[@text='Make Payment']")))
makepaymentbutton.click()

phone = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((MobileBy.XPATH, "//*[@text='Phone']")))
phone.click()
phone.send_keys("1234567890")

name = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((MobileBy.XPATH, "//*[@text='Name']")))
name.click()
name.send_keys("Vanessa Matteo")

selectcountrybutton = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((MobileBy.XPATH, "//*[@text='Select']")))
selectcountrybutton.click()

country = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((MobileBy.XPATH, "//*[@text='USA']")))
country.click()

# app = "C:\\Users\\CorinneJoyceReloj\\Documents\\BPI PROJECT\\TESTING\\SDET TRAINING\\Mobile Automation Testing\\Android.SauceLabs.Mobile.Sample.app.2.7.1.apk"
# print(app)
#
# desired_caps = {
#     'deviceName': 'Android Device',
#     'deviceId': '5554',
#     'platformName': 'Android',
#     'appPackage': 'com.swaglabsmobileapp',
#     'appActivity': 'com.swaglabsmobileapp.MainActivity',
#     'app': app
# }
#
# print(desired_caps)
# #default appium server: 127.0.0.1
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
# print("Application launched successfully")

actions = TouchAction(driver)
#move to element
#actions.move_to(usernamefield, 10, 10)

#double click
#actions.move_to(usernamefield)
#actions.double_click()

#single tap
actions.tap(usernamefield)
actions.perform()

#double tap
actions.double_tap(usernamefield)
actions.perform()

driver.back()
driver.refresh()
driver.forward()

#tap and hold
actions.tap_and_hold(usernamefield)
actions.perform()

#selecting the checkbox
driver.find_element_by_accessibility_id('abc').is_selected()

#to reset the application in the device
driver.reset()

#to close the app
driver.close_app()

#to remove app
driver.remove_app()

#to hide the keyboard
driver.hide_keyboard()

#whether keyboard is available
driver.is_keyboard_shown()

#whether device is locked
driver.is_locked()

#check notifications
driver.open_notifications()

#to get the time of the device
driver.get_device_time()

#access the location of device
driver.location()

#delete cookies from the device
driver.delete_all_cookies()

#orientation
driver.orientation = "LANDSCAPE"
driver.orientation = "PORTRAIT"