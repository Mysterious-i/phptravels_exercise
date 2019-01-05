import sys
import time

import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.common.exceptions import WebDriverException as driverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

# Constants
LOGIN_PAGE = 'https://www.phptravels.net/login'
ACC_PAGE = 'https://www.phptravels.net/account'
LOGIN_EMAIL = "//input[@name='username']"
LOGIN_PASSWORD = "//input[@name='password']"


@pytest.fixture(
    params=[
        {"username": "user@phptravels.com"},
        {"password": "demouser"},
    ]
)
def credentials():
    user


# Scenarios
# Here we use pytest to parametrize the test with the parameters table

scenarios('../features/login.feature')


@given(parsers.parse('the phptravels Login page is displayed'))
def login_page(browser):
    browser.get(LOGIN_PAGE)
    print >> sys.stdout, "In the login page"
    return browser.title


@given("I am logged in")
def logged_in(browser):
    print >> sys.stderr, browser.current_url
    input_credts(browser, 'user@phptravels.com', 'demouser')
    time.sleep(1)
    # print >> sys.stderr, "username:" +
    print >> sys.stderr, "im logged in and current url " + browser.current_url
    # // *[ @ id = "body-section"] / div[1] / div / div / div[1] / h3
    # return browser.find_element_by_name('login.png')


@given("I am an authenticated user in the Home page")
def after_login(browser, home_page):
    print >> sys.stderr, "redirecting back to home page"
    pass


@when("I select the Login option from the My Account drop down")
def back_home(browser):
    print >> sys.stderr, 'current url ' + browser.current_url
    # //*[@id="li_myaccount"]
    menu_xpath = "//nav[contains(@class,'navbar-default')]//li[@id='li_myaccount']//a[contains(@class,'dropdown-toggle')]"
    my_acc = EC.element_to_be_selected((By.CSS_SELECTOR, 'nav.navbar-default li#li_myaccount a.dropdown-toggle'))
    #  selector = #li_myaccount
    try:
        WDW(browser, 2).until(EC.element_to_be_clickable((By.XPATH, menu_xpath))).click()

    except driverException:
        print >> sys.stderr, "the element" + browser.error_handler
        print >> sys.stderr, "couldnt find My Account Button \n"
    try:
        WDW(browser, 2).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()

    except driverException:
        print >> sys.stderr, "the element" + str(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
        print >> sys.stderr, " i couldnt click login  \n"
    time.sleep(1)
    # WDW(browser, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "My Account"))).click()

    # WDW(browser, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()


@when('I input <email> and <password>')
def input_credts(browser, email, password):
    assert "Login" in browser.page_source
    print >> sys.stderr, browser.current_url
    try:
        elem = browser.find_element_by_xpath(LOGIN_EMAIL)
        elem.send_keys(email)
        elem = browser.find_element_by_xpath(LOGIN_PASSWORD)
        elem.send_keys(password)
        elem.send_keys(Keys.RETURN)
    except driverException:
        print >> sys.stderr, "email entered:" + email + "\npassword entered:" + password

    # Make sure you wait for the page to load completely
    time.sleep(3)
    return browser


@when(parsers.parse('I input incorrect email or password'))
def invalid_credts(browser):
    input_credts(browser, '', 'whatever')


@then(parsers.parse('I should see the Login page with a warning message'))
def failed_login(browser):
    print >> sys.stderr, "redirecting back to login page"
    assert "Login" in browser.title
    assert browser.current_url.__contains__(LOGIN_PAGE)
    time.sleep(3)
    assert "Invalid Email or Password" in browser.page_source


@then(parsers.parse('I should be redirected to my Account page'))
def my_account(browser):
    assert "My Account" in browser.title
    assert browser.current_url.__contains__(ACC_PAGE)
