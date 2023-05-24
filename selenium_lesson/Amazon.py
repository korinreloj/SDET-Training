from selenium import webdriver

PATH = "C:\\Users\\CorinneJoyceReloj\\PycharmProjects\\SDETTrainingProject\\driver\\chromedriver.exe"

#to open/launch chrome browser
driver = webdriver.Chrome(PATH)
url = "https://www.amazon.com/"

# open amazon
driver.get(url)
driver.maximize_window()

search_bar = driver.find_element_by_xpath("//*[@id='twotabsearchtextbox']")
search_bar.send_keys("electronics")

submit_button = driver.find_element_by_xpath("//*[@id='nav-search-submit-button']")
submit_button.click()

#results
item1_name = driver.find_element_by_xpath("//*[@id='search']/div[1]/div/div[1]/div/span[3]/div[2]/div[2]/div/span/div/div/div/div/div/div[1]/h2/a/span").text
print(item1_name)

item2_name = driver.find_element_by_xpath("//*[@id='search']/div[1]/div/div[1]/div/span[3]/div[2]/div[3]/div/span/div/div/div/div[1]/h2/a/span").text
print(item2_name)

item3_name = driver.find_element_by_xpath("//*[@id='search']/div[1]/div/div[1]/div/span[3]/div[2]/div[4]/div/span/div/div/div/div[1]/h2/a/span").text
print(item3_name)

item4_name = driver.find_element_by_xpath("//*[@id='search']/div[1]/div/div[1]/div/span[3]/div[2]/div[5]/div/span/div/div/div/div[1]/h2/a/span").text
print(item4_name)

driver.close()