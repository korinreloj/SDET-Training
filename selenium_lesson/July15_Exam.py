import time
from selenium import webdriver
from selenium.webdriver import ActionChains

PATH = "C:\\Users\\CorinneJoyceReloj\\PycharmProjects\\SDETTrainingProject\\driver\\chromedriver.exe"

#to open/launch chrome browser
driver = webdriver.Chrome(PATH)
url = "http://hrm.syntaxtechs.net/humanresources/symfony/web/index.php/auth/login"

driver.get(url)
driver.maximize_window()

valid_username = "Admin"
valid_password = "Hum@nhrm123"

#login page
username_input = driver.find_element_by_xpath("//*[@id='txtUsername']")
username_input.send_keys(valid_username)
time.sleep(1)

password_input = driver.find_element_by_xpath("//*[@id='txtPassword']")
password_input.send_keys(valid_password)
time.sleep(1)

login_button = driver.find_element_by_xpath("//*[@id='btnLogin']")
login_button.click()
time.sleep(1)

#home page
action = ActionChains(driver)
PIM_tab = driver.find_element_by_css_selector("#menu_pim_viewPimModule > b")
action.move_to_element(PIM_tab).click().perform()
time.sleep(2)

#search page
employee_id = "17551"

id_input = driver.find_element_by_xpath("//*[@id='empsearch_id']")
id_input.send_keys(employee_id)
time.sleep(1)

search_button = driver.find_element_by_xpath("//*[@id='searchBtn']")
search_button.click()
time.sleep(1)

#verify lastname and firstname
lastName = "fsdfs"
firstName = "sdjkbfgksgbk dsfsd"

result_lastName = driver.find_element_by_xpath("//*[@id='resultTable']/tbody/tr/td[4]")
result_lastName_value = result_lastName.text
assert result_lastName_value == lastName
print("Passed:::Last Name: " + result_lastName_value)

result_firstName = driver.find_element_by_xpath("//*[@id='resultTable']/tbody/tr/td[3]")
result_firstName_value = result_firstName.text
assert result_firstName_value == firstName
print("Passed:::First Name: " + result_firstName_value)

driver.quit()
