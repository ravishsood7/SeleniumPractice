# ---------------------------------------------------------------------------------------
# Locators
# 1. by id and by name
# 2. by linkText and partial LinkText
# 3. by className and tagName

# ---------------------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Drivers/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad Carbon Laptop")
driver.find_element(By.LINK_TEXT,"Register").click()