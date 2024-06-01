# Go to Home Page
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://magento.softwaretestingboard.com/")
driver.maximize_window()
# Click on "Create an Account"
driver.find_element(By.XPATH, "//div[@class='panel header']//a[normalize-space()='Create an Account']").click()

# Create new user - personal information
# Enter First Name
driver.find_element(By.XPATH, "//input[@id='firstname']").send_keys("Pradnya")
# Enter Last Name
driver.find_element(By.CSS_SELECTOR, "#lastname").send_keys("Chougule")
# Enter Email ID
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("chougule.pradny1@gmail.com")
# Enter Password
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("Pradnya@123")
print(driver.find_element(By.XPATH, "//span[@id='password-strength-meter-label']").text)
# password strength - No password, Very Strong, Weak, Medium.
# Confirm Password
driver.find_element(By.CSS_SELECTOR, "#password-confirmation").send_keys("Pradnya@123")
# Click on Create an account button.
driver.find_element(By.XPATH, "//button[@class='action submit primary']").click()
if driver.title == "My Account":
    print("Account created successfully")
    print(driver.find_element(By.CSS_SELECTOR, ".message-success.success.message").text)
    driver.find_element(By.CSS_SELECTOR, "#ui-id-3").click()
else:
    driver.save_screenshot("C:\\Users\\nandr\\PycharmProjects\\MagentoPractice\\ScreenshotsFail\\AcountCreateFail.jpg")
time.sleep(5)