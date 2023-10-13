# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.dominos.ca/en/")
time.sleep(3)
menulist =driver.find_element("xpath","/html/body/header/nav[1]/div[1]/ul/li[3]/a")
menulist.click()
time.sleep(3)
pizza_link = driver.find_element("xpath","/html/body/div[4]/div[2]/div/div[3]/div/div[1]/a")
pizza_link.click()
time.sleep(3)
selected_pizza =driver.find_element("xpath","/html/body/div[4]/div[2]/div/div[3]/section[1]/div/div/div[1]/a/img")
selected_pizza.click()
time.sleep(3)
carryout =driver.find_element("xpath","/html/body/div[3]/div[3]/div/div/div[2]/form/div/div[1]/label[2]")
carryout.click()
time.sleep(3)
LocationBox =driver.find_element("xpath","/html/body/div[3]/div[3]/div/div/div[2]/form/div/div[2]/fieldset/div[3]/div[1]/div[2]/div/div/div/div/div[4]/div/div/input")
LocationBox.send_keys("Conestoga College Waterloo Campus, University Avenue, Waterloo, ON")

#searchButton =driver.find_element("xpath","/html/body/div[3]/div[3]/div/div/div[2]/form/div/div[2]/fieldset/div[3]/div[1]/div[2]/div/div/div/div/div[4]/div/div/button")
#searchButton.click()


#LocationBox.send_keys(Keys.RETURN)
time.sleep(3)
#assert "Conestoga College Waterloo Campus, University Avenue, Waterloo, ON" in driver.title

orderitem =driver.find_element("xpath","/html/body/div[3]/div[3]/div/div/div[2]/form/div/div[3]/div[2]/div/div[2]/div/div[4]/div/div/div/button")
orderitem.click()
time.sleep(3)

addtocart = driver.find_element("xpath","/html/body/div[5]/div/section/div/div/ol/li[7]/aside/section/div/button")
addtocart.click()
time.sleep(3)

cheese_selection =driver.find_element("xpath","/html/body/div[5]/div/section/div/div/div/div/button[1]")
cheese_selection.click()
time.sleep(3)

check_out =driver.find_element("xpath","/html/body/div[3]/div[2]/aside/div[1]/a")
check_out.click()
time.sleep(3)

no_thanks = driver.find_element("xpath","/html/body/div[27]/section/div/div[2]/div/a")
no_thanks.click()
time.sleep(3)

continue_checkout =driver.find_element("xpath","/html/body/div[3]/div[3]/div/div/div[3]/aside/div[3]/div[1]/a")
continue_checkout.click()
time.sleep(3)



# Verifying that the laptop has been added to the cart
# cart_count = driver.find_element("id","nav-cart-count")
# assert cart_count.text == "1"
# cart_count.click()

# Closing the webdriver
driver.close()
