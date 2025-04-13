# ---------------------------------------------------------------------------------------
# Problem:
# Selenium was throwing `NoSuchElementException` when trying to locate the username field.
# This happened because the element wasn't loaded in the DOM at the time of access.
#
# Solution:
# Replaced direct `find_element` calls with explicit waits using `WebDriverWait` and
# `expected_conditions`. This ensures Selenium waits until the element is present before interacting.
# ---------------------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#
# service_obj = Service("C:/Drivers/chromedriver-win64/chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Wait for username field and send keys
wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("admin123")
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.orangehrm-login-button"))).click()

# Wait a bit to ensure page loads after login
wait.until(EC.title_contains("OrangeHRM"))

act_title = driver.title
exp_title = "OrangeHRM"

print("Actual Title:", act_title)
print("Expected Title:", exp_title)

if act_title == exp_title:
    print("Login Test Passed ✅")
else:
    print("Login Test Failed ❌")

driver.quit()
