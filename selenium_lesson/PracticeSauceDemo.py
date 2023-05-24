from selenium import webdriver
from selenium.webdriver.support.select import Select

PATH = "C:\\Users\\CorinneJoyceReloj\\PycharmProjects\\SDETTrainingProject\\driver\\chromedriver.exe"

#to open/launch chrome browser
driver = webdriver.Chrome(PATH)
url = "https://www.saucedemo.com/"

# open swaglab
driver.get(url)
driver.maximize_window()

# login via standard credentials
userName = driver.find_element_by_xpath("//input[@name='user-name']")
userName.send_keys("standard_user")
driver.implicitly_wait(2)

password = driver.find_element_by_xpath("//input[@type='password']")
password.send_keys("secret_sauce")
driver.implicitly_wait(2)

loginButton = driver.find_element_by_xpath("//*[@value='Login']")
loginButton.click()
driver.implicitly_wait(3)

# select first value from the dropdwon (filter)
selectFilter = Select(driver.find_element_by_css_selector("select.product_sort_container"))

# select first item from the list
selectFilter.select_by_index(0)

# get the name of this(first) item
firstItem = driver.find_element_by_xpath("//*[@id='inventory_container']/div/div[1]/div[2]/div[1]/a/div")
firstItemName = firstItem.text
print("First item name: " + firstItemName)

# add to cart first item
addToCartButton = driver.find_element_by_xpath("//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/button")
addToCartButton.click()

# click on cart icon and verify the item is the same which you have selected
cartButton = driver.find_element_by_css_selector("a.shopping_cart_link")
cartButton.click()

cartItem = driver.find_element_by_xpath("//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/a/div[@class='inventory_item_name']")
cartItemName = cartItem.text
assert firstItemName == cartItemName
print("Passed: " + firstItemName + " == " + cartItemName)

# remove the item from the cart
removeItemButton = driver.find_element_by_xpath("//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/button")
removeItemButton.click()

# click on continue shopping icon
continueShoppingButton = driver.find_element_by_css_selector("button#continue-shopping")
continueShoppingButton.click()

# select second item from the suggested items
secondItem = driver.find_element_by_xpath("//*[@id='inventory_container']/div/div[2]/div[2]/div[1]/a/div")
secondItemName = secondItem.text
print("Second item name: " + secondItemName)

#add to cart second item
addToCartButton = driver.find_element_by_xpath("//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/button")
addToCartButton.click()

# verify it in the cart
cartButton = driver.find_element_by_css_selector("a.shopping_cart_link")
cartButton.click()

cartItem = driver.find_element_by_xpath("//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/a/div[@class='inventory_item_name']")
cartItemName = cartItem.text
assert secondItemName == cartItemName
print("Passed: " + secondItemName + " == " + cartItemName)

# and select hamburger menu
hamburgerButton = driver.find_element_by_css_selector("button#react-burger-menu-btn")
hamburgerButton.click()

# and click on logout option
logoutButton = driver.find_element_by_css_selector("a#logout_sidebar_link")
logoutButton.click()

driver.quit()