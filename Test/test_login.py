
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    # Setup the ChromeDriver instance
    driver = webdriver.Chrome()

    # Make the driver quit after tests
    yield driver
    driver.quit()


def test_login(driver):
    # Open  the website
    username = 'test_user0000'
    driver.get("https://www.demoblaze.com/")

    # Click on the login button
    driver.find_element(By.ID, "login2").click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "loginusername")))

    # Assert that the login and password fields are present
    assert driver.find_element(By.ID, "loginusername").is_displayed()
    assert driver.find_element(By.ID, "loginpassword").is_displayed()

    # Enter credentials and log in
    driver.find_element(By.ID, "loginusername").send_keys(username)
    driver.find_element(By.ID, "loginpassword").send_keys("Test1234")
    driver.find_element(By.XPATH, "//*[@id='logInModal']/div/div/div[3]/button[2]").click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "logout2")))

    # Assert that logout button and welcome message are displayed
    assert driver.find_element(By.ID, "logout2").is_displayed()
    assert f"Welcome {username}" in driver.page_source





