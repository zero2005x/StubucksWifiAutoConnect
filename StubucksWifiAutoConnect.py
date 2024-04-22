import logging
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# 初始化Tkinter，但不顯示主窗口
# Initialize Tkinter, but do not display the main window
Tk().withdraw()

# 函數檢查文件是否存在且正確
# Function to check if the file exists and is correct
def select_file(prompt, initialdir, filetypes):
    path = askopenfilename(title=prompt, initialdir=initialdir, filetypes=filetypes)
    if path:
        return path
    else:
        logging.error("File selection cancelled.")
        exit()

#指定你的geckodriver的位置
# Specify the path to your geckodriver
# Change this to your geckodriver path
geckodriver_path = r"C:\Users\liangtinglin\Documents\python\StubucksWifiAutoConnect\geckodriver.exe"  

#指定你的Firefox的位置
# Specify the path to your Firefox
# Change this to your Firefox path
# Change this to your Firefox path
firefox_binary_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"  


# 檢查文件是否存在和正確
# Check if the files exist and are correct
if not os.path.isfile(geckodriver_path) or not "geckodriver.exe" in geckodriver_path:
    logging.warning("Invalid or missing geckodriver. Please select geckodriver.exe.")
    geckodriver_path = select_file("Select geckodriver.exe", "/", [("Executable", "*.exe")])

if not os.path.isfile(firefox_binary_path) or not "firefox.exe" in firefox_binary_path:
    logging.warning("Invalid or missing Firefox binary. Please select firefox.exe.")
    firefox_binary_path = select_file("Select firefox.exe", "/", [("Executable", "*.exe")])

# Setup Firefox service
service = FirefoxService(executable_path=geckodriver_path)

# Set Firefox options
options = webdriver.FirefoxOptions()
options.add_argument('--headless')  # Run in headless mode
options.binary_location = firefox_binary_path

# Initialize the WebDriver
driver = webdriver.Firefox(service=service, options=options)

try:
    # Navigate to the Starbucks Wi-Fi login page
    driver.get("http://172.16.8.100:9997/user/guest_tou.asp?origurl=http%3a%2f%2fwww%2emsftconnecttest%2ecom%2fredirect&langname=zh%5fTW&logo=%2fwritable%2fdata%2fwsgclient%2flogo%5f1")  # Replace with the actual URL if different

    # Wait for the "Accept and Continue" button to be clickable
    accept_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, "acceptBtn"))
    )

    # Click the "Accept and Continue" button
    accept_button.click()
    logging.info("Successfully connected to Starbucks Wi-Fi.")

except TimeoutException:
    logging.error("Timeout while trying to connect to Starbucks Wi-Fi.")
except Exception as e:
    logging.error(f"An error occurred: {e}")
finally:
    # Close the browser
    driver.quit()
