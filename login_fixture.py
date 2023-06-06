import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def login(driver):
    # Open the website
    driver.get("https://www.demoblaze.com/")

    # Click on the login button
    driver.find_element(By.ID, "login2").click()

    # Wait for the username field to become visible
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "loginusername")))

    # Enter credentials and log in
    driver.find_element(By.ID, "loginusername").send_keys("test_user0000")
    driver.find_element(By.ID, "loginpassword").send_keys("Test1234")

    # Click the login button
    driver.find_element(By.XPATH, "//*[@id='logInModal']/div/div/div[3]/button[2]").click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "logout2")))

    return driver
