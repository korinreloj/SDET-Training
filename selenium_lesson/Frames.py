from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\\Users\\CorinneJoyceReloj\\PycharmProjects\\SDETTrainingProject\\driver\\chromedriver.exe"

#to open/launch chrome browser
driver = webdriver.Chrome(PATH)
# url = "https://the-internet.herokuapp.com/nested_frames"
# url = "https://demoqa.com/frames"
#
# driver.get(url)
# driver.maximize_window()
#
# #switch to the frame by framename
# # we can also switch via inside of the frame
# driver.switch_to.frame("frame2")
# time.sleep(1)
#
# element_In_frame = driver.find_element_by_xpath("//*[@id='sampleHeading']")
# message = element_In_frame.text
# print(message)
#
# #to move to default view
# driver.switch_to.default_content()
# time.sleep(2)
#
# driver.quit()

#---------------------------------------------------------------
# automate one scenario with iframe and select locators within the frame
url = "https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame"

driver.get(url)
driver.maximize_window()

driver.switch_to.frame("globalSqa")
time.sleep(1)

page_title = driver.find_element_by_xpath("//*[@id='wrapper']/div[1]/div[1]/div/div/div/div[1]/a[2]/span[text()='Trainings']")
title = page_title.text
print(title)

filter = driver.find_element_by_xpath("//*[@id='current_filter']")
action = ActionChains(driver)
action.move_to_element(filter).click().perform()
time.sleep(2)

automation_filter = driver.find_element_by_xpath("//*[@id='filter_list']/li[1]/div")
action.move_to_element(automation_filter).click().perform()
time.sleep(2)

second_result = driver.find_element_by_xpath("//*[@id='portfolio_items']/div[8]/a/div/div/div[2]/div/div/h3")
second_result_title = second_result.text
print(second_result_title)
second_result_link = driver.find_element_by_xpath("//*[@id='portfolio_items']/div[8]")
second_result_link.click()
time.sleep(2)

#to move to default view
driver.switch_to.default_content()
time.sleep(2)
default_page_title = driver.find_element_by_xpath("//div[@class='page_heading']/h1[text()='Frames And Windows']")
title = default_page_title.text
print(title)

driver.quit()