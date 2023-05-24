import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

app = "C:\\Users\\CorinneJoyceReloj\\Documents\\BPI PROJECT\\TESTING\\SDET TRAINING\\Mobile Automation Testing\\Android.SauceLabs.Mobile.Sample.app.2.7.1.apk"
print(app)

desired_caps = {
    'deviceName': 'Android Device',
    'deviceId': '5554',
    'platformName': 'Android',
    'appPackage': 'com.swaglabsmobileapp',
    'appActivity': 'com.swaglabsmobileapp.MainActivity',
    'app': app
}

print(desired_caps)
#default appium server: 127.0.0.1
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
print("Application launched successfully")

usernamefield = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((MobileBy.XPATH, "//*[@text='Username']")))
usernamefield.click()
usernamefield.send_keys("problem_user")

passwordfield = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((MobileBy.XPATH, "//*[@text='Password']")))
passwordfield.click()
passwordfield.send_keys("secret_sauce")

loginbutton = driver.find_element_by_xpath("//*[@text='LOGIN']")
loginbutton.click()

addToCart1 = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((MobileBy.XPATH, "//*[@text='ADD TO CART']")))
addToCart1.click()

shoppingCart = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((MobileBy.XPATH, "//*[@index='3']")))
shoppingCart.click()
print("cart")

hamburger_button = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((MobileBy.XPATH, "//*[@content-desc='test-Menu']")))
hamburger_button.click()
time.sleep(2)

logout = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((MobileBy.XPATH, "//*[@text='LOGOUT']")))
logout.click()
time.sleep(2)

login_page = driver.find_element_by_xpath("//*[@content-desc='test-Login']")
assert login_page.is_displayed()
print("Test passed")