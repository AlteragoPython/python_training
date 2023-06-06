from selenium.webdriver.common.by import By

class Locators(object):
    Username_field = (By.NAME,'user-name')
    Password_field = (By.XPATH,'//*[@id="password"]')
    Login_button = (By.ID,'login-button')