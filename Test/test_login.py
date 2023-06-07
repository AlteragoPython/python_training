
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_fixture import login
import time

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


def test_product_selection(login):
    driver = login
    # Step 1: Click on Monitors category
    driver.find_element(By.LINK_TEXT, "Monitors").click()
    time.sleep(2)

    # Step 2: Click on the product with the highest price on the page
    products = driver.find_elements(By.CSS_SELECTOR, "div.card-block")
    highest_price = 0
    highest_price_product = None
    for product in products:
        price = float(product.find_element(By.CSS_SELECTOR, "h5").text.replace('$', ''))
        if price > highest_price:
            highest_price = price
            highest_price_product = product
    highest_price_product_text = highest_price_product.find_element(By.CSS_SELECTOR, "h4 a").text
    highest_price_product.find_element(By.CSS_SELECTOR, "h4 a").click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2")))



    # Assert that we're on the product page
    assert driver.find_element(By.CSS_SELECTOR, "h4").is_displayed()

    # Step 3: Click on Add to cart button
    driver.find_element(By.LINK_TEXT, "Add to cart").click()

    # Step 4: Click on Cart button
    driver.find_element(By.ID, "cartur").click()
    time.sleep(2)

    # Assert that the product is in the cart
    cart_items = driver.find_elements(By.CSS_SELECTOR,"tr.success")
    assert any(highest_price_product_text in item.text for item in cart_items), f"{highest_price_product_text} is not found in the cart"






