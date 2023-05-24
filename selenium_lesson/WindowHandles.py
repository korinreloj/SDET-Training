from selenium import webdriver
import time

PATH = "C:\\Users\\CorinneJoyceReloj\\PycharmProjects\\SDETTrainingProject\\driver\\chromedriver.exe"

#to open/launch chrome browser
driver = webdriver.Chrome(PATH)
url = "https://the-internet.herokuapp.com/windows"

# driver.get(url)
# driver.maximize_window()
#
# time.sleep(2)
#
# link_text = driver.find_element_by_link_text("Click Here")
# link_text.click()
#
# time.sleep(2)
#
# #print the window handle in focus; will return which window you are currently at
# print(driver.current_window_handle)
#
# #switch to first child window; index does not start at zero because it is the window number
# first_child = driver.window_handles[1]
# driver.switch_to.window(first_child)
#
# #finding the element on the child window
# child_window_element = driver.find_element_by_xpath("/html/body/div/h3")
#
# message = child_window_element.text
# print(message)
#
# driver.quit()
#it will only close the first child window
# driver.close()

#--------------------------------------------
# Handle 3 windows in the webpage
driver.get(url)
driver.maximize_window()

parent_window = driver.current_window_handle
print("Parent window: " + parent_window)

link_text = driver.find_element_by_link_text("Click Here")
link_text.click()

time.sleep(2)

#first child
first_child = driver.window_handles[1]
driver.switch_to.window(first_child)
print("First child: " + driver.current_window_handle)
time.sleep(2)

#back to parent
driver.switch_to.window(parent_window)
time.sleep(2)
link_text = driver.find_element_by_link_text("Click Here")
link_text.click()

#second child
second_child = driver.window_handles[2]
driver.switch_to.window(second_child)
print("Second child: " + driver.current_window_handle)
time.sleep(2)

#back to parent
driver.switch_to.window(parent_window)
time.sleep(2)
link_text = driver.find_element_by_link_text("Click Here")
link_text.click()

#second child
third_child = driver.window_handles[3]
driver.switch_to.window(third_child)
print("Third child: " + driver.current_window_handle)
time.sleep(2)

driver.switch_to.window(first_child)
time.sleep(2)

driver.quit()

