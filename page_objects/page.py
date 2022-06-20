from page_objects.element import BasePageElement
from page_objects.locators import MainPageLocators
from selenium import webdriver

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = 'p'

class SetTextElement(BasePageElement):
    """This class set the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = 'q'


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver : webdriver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here"""

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def is_title_matches(self, title):
        """Verifies that the hardcoded text "Ridely - Ask Expert" appears in page title"""
        return title in self.driver.title

    def click_sign_in_button(self):
        """Triggers the sign in process"""
        element = self.driver.find_element(*MainPageLocators.SIGN_IN_BUTTON)
        element.click()

    def get_email_field(self):
        return self.driver.find_element(*MainPageLocators.EMAIL_FIELD)

    def insert_email(self, email):
        """Inserts email to the email field"""
        email_field = self.get_email_field()
        email_field.send_keys(email)

    def clear_email_field(self):
        """Inserts email to the email field"""
        email_field = self.get_email_field()
        email_field.find_element(*MainPageLocators.EMAIL_FIELD).clear()
    
    def get_password_field(self):
        """Returns webdriver element with a password field"""
        return self.driver.find_element(*MainPageLocators.PASSWORD_FIELD)

    def insert_passwd(self, passwd):
        """Inserts pasword to the passwd field"""
        password_el = self.get_password_field()
        element = password_el.send_keys(passwd)

    def clear_passwd_field(self):
        """Inserts pasword to the passwd field"""
        password_el = self.get_password_field()
        password_el.clear()

    def get_login_page_logo_image(self):
        """Returns logo element"""
        logo = self.driver.find_element(*MainPageLocators.LOGO)
        return logo

    