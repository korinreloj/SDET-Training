import time

from selenium import webdriver
from time import sleep

PATH = "C:\\Users\\CorinneJoyceReloj\\PycharmProjects\\SDETTrainingProject\\driver\\chromedriver.exe"

#to open/launch chrome browser
driver = webdriver.Chrome(PATH)
url = "https://www.youtube.com/"
#to open the app in browser
driver.get(url)

#to maximize window
driver.maximize_window()

#application url
print(driver.current_url)

#application title
print(driver.title)

expectedTitle= "YouTube"
#to verify the operation we use assert
assert expectedTitle == driver.title
print("My test passed")

#to verify the operation we use assert
assert url == driver.current_url
print("both urls match")

#to clear cache from the browser
driver.delete_all_cookies()

#To get the browser back
driver.back()

#To get the browser forward
driver.forward()

#refresh the browser
driver.refresh()

#navigate to
#driver.navigate().to("https://www.google.com/")