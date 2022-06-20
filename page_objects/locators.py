from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, '.mat-raised-button')
    EMAIL_FIELD = (By.ID, 'mat-input-0')
    PASSWORD_FIELD = (By.ID, 'mat-input-1')
    LOGO = (By.CLASS_NAME, 'login-logo-svg')