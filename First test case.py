from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Define the path to the ChromeDriver
service = Service(r"C:\Users\namratab\Documents\chromedriver-win64\chromedriver.exe")

# Initialize the WebDriver using the Service object
driver = webdriver.Chrome(service=service)

# Open the website
driver.get("https://opensource-demo.orangehrmlive.com/")

# enter username
driver.find_element(By.NAME, "username").send_keys("Admin")

# Enter password
driver.find_element(By.NAME, "password").send_keys("admin123")

# Click the login button
driver.find_element(By.XPATH, "//button[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

act_title=driver.title
exp_title="OrangeHRM"

if act_title==exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

driver.close()

