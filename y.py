from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the path to the ChromeDriver
service = Service(r"C:\Users\namratab\Documents\chromedriver-win64\chromedriver.exe")

# Initialize the WebDriver using the Service object
driver = webdriver.Chrome(service=service)

# Open the website
driver.get("https://opensource-demo.orangehrmlive.com/")

# Wait for the username field to be present
wait = WebDriverWait(driver, 10)
username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
username_field.send_keys("Admin")

# Enter password
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("admin123")

# Click the login button
login_button = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
login_button.click()

# Wait for the page to load and verify the title
wait.until(EC.title_contains("OrangeHRM"))
act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

driver.close()
