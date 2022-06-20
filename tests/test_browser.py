import pytest
import logging
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.page import MainPage

LOG = logging.getLogger('Test login page')


    

class TestRidleyLoginPage():
    """A test class with collection of the test for a login page"""


    @pytest.mark.id_1
    def test_title_presentation(self, browser):
        """Test title present on a login page"""
        main_page = MainPage(browser)
        assert main_page.is_title_matches("Ridely - Ask Expert"), "Ridely - Ask Expert title doesn't match."
        
    @pytest.mark.id_2
    def test_login_with_incorrect_credentials(self, browser : WebDriver):
        """
        Test if proper message is displayed when login with incorrect credentials
        """
        main_page = MainPage(browser)
        main_page.insert_email('test@test.com')
        main_page.insert_passwd('passwd123')
        main_page.click_sign_in_button()
        try:
            alert = browser.switch_to_alert()
        except Exception as e:
            LOG.exception(e)
        if alert: 
            assert alert.text == 'Invalid credentials', "Invalid credentials alert doesn't show up"
        else:
            pytest.fail('Expected allert occurrs on try to login with incorrect credentials')

    @pytest.mark.id_3
    @pytest.mark.parametrize("test_input,expected", [('test', 'ng-invalid'), ("", "ng-invalid"), ("test@", "ng-invalid"),
                            ("test@", "ng-invalid"), ('1', "ng-invalid")])
    def test_highlight_invalid_email_fields(self, browser : WebDriver, test_input, expected):
        """
        Function tests if fields with missing data is highlighter with a red color
        """
        main_page = MainPage(browser)
        main_page.clear_email_field()
        main_page.insert_email(test_input)
        email_field = main_page.get_email_field()
        assert expected in email_field.get_attribute('class')
        
    @pytest.mark.id_4
    @pytest.mark.parametrize("test_input,expected", [('test@test.com', 'ng-valid')])
    def test_valid_email(self, browser : WebDriver, test_input,expected):
        """Function test if email field is not highlighted if proper email is inserted"""
        main_page = MainPage(browser)
        main_page.clear_email_field()
        main_page.insert_email(test_input)
        email_field = main_page.get_email_field()
        assert expected in email_field.get_attribute('class')

    @pytest.mark.id_5
    def test_valid_password_field(self, browser : WebDriver):
        """function tests if valid password does not highlight a field """
        main_page = MainPage(browser)
        main_page.clear_passwd_field()
        main_page.insert_passwd('password')
        password_field = main_page.get_password_field()
        assert 'ng-valid' in password_field.get_attribute('class')

    @pytest.mark.id_6
    def test_invalid_password_field(self, browser : WebDriver):
        """Function that tests invalid password field"""
        main_page = MainPage(browser)
        main_page.clear_passwd_field()
        main_page.insert_passwd('')
        password_field = main_page.get_password_field()
        assert 'ng-invalid' in password_field.get_attribute('class')

    @pytest.mark.id_7
    def test_if_logo_displed(self, browser : WebDriver):
        """Function that tests if logo is displayed"""
        main_page = MainPage(browser)
        logo = main_page.get_login_page_logo_image()
        assert logo.size.get('height') > 0, 'Image height should be greather than 0'
        assert logo.size.get('width') > 0, 'Image width should be greather 0'

