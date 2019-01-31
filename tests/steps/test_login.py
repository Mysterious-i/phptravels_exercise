import sys
import time

import requests
from pytest_bdd import scenarios, given, when, then
from selenium.common.exceptions import WebDriverException as driverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

from commons import get_page_url, PAGE_LOAD_WAIT, ELEMENT_LOCATORS, CREDENTIALS

scenarios('../features/login.feature')


# scenarios('../features/search_hotels.feature')
# Constants


# Scenarios
# Here we use pytest to parametrize the test with the parameters table

# When step definitions
@given('the phptravels Login page is displayed')
def login_page(browser, report_logger):
    """
    Args:
        browser:
        report_logger:
    """
    browser.get(get_page_url('login_path'))
    assert EC.title_contains('Login')
    report_logger.info("___current title %s" % browser.title)
    report_logger.info("___current url %s" % browser.current_url)
    pass
    # return "browser title "+browser.title


@given("the user is logged in")
def log_in(browser, report_logger):
    """
    Args:
        browser:
        report_logger:
    """
    report_logger.info("___current title %s" % browser.title)
    report_logger.info("___current url %s" % browser.current_url)
    report_logger.warning(("__ user is logging in with the following credentials email:{} password:{}".format(
                          CREDENTIALS['valid'].get('email'), CREDENTIALS['valid'].get('password'))))
    input_credts(browser, CREDENTIALS['valid'].get('email'), CREDENTIALS['valid'].get('password'), report_logger)
    report_logger.warning("current browser.title %s" % browser.title)
    # time.sleep (1)
    # print >> sys.stderr, "username:" +
    # report_logger.warning("___should be logged in with url"
    # // *[ @ id = "body-section"] / div[1] / div / div / div[1] / h3
    # return browser.find_element_by_name('login.png')


# homepage
@given('there is an authenticated user in the home_page')
def after_login(browser, report_logger):
    """
    Args:
        browser:
        report_logger:
    """
    print >> sys.stderr, "logged in "
    browser.get(get_page_url('home'))
    report_logger.debug(browser.current_url)
    report_logger.warning("should be redirecting back to home page")
    pass


@given('there is an authenticated user in the account_page')
def afn(browser, report_logger):
    """
    Args:
        browser:
        report_logger:
    """
    report_logger.info("current title %s" % browser.title)
    report_logger.info("current url %s" % browser.current_url)

    browser.get(get_page_url('my_account_path'))
    report_logger.warning("should be redirecting to account_page %s" % browser.current_url)
    pass


# When step definitions
# @when("I select the Login option from the My Account drop down")
@when("the user selects the Login option from the My Account drop down")
def back_home(browser, report_logger):
    """
    Args:
        browser:
        report_logger:
    """
    cur_title = browser.title
    cur_url = browser.current_url

    report_logger.info("current title %s" % cur_title)
    report_logger.info("current url %s" % browser.current_url)
    if cur_url.__contains__("account"):
        browser.get(get_page_url('home'))

    # print >> sys.stderr, 'current url ' + browser.current_url
    # //*[@id="li_myaccount"]
    # menu_xpath =
    # "//nav[contains(@class,'navbar-default')]//li[@id='li_myaccount']//a[contains(@class,'dropdown-toggle')]"
    # my_acc = EC.element_to_be_selected((By.CSS_SELECTOR, 'nav.navbar-default li#li_myaccount a.dropdown-toggle'))
    #/html/body/nav/div/div[2]/ul[2]/ul/li[1]/ul/li[1]
    #  selector = #li_myaccount
    try:
        WDW(browser, PAGE_LOAD_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, ELEMENT_LOCATORS['myaccount_dd_menu']))).click()
        WDW(browser, PAGE_LOAD_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, ELEMENT_LOCATORS['myaccount_dd_menu_item1']))).click()
        browser.implicitly_wait(PAGE_LOAD_WAIT)

    except driverException:
        report_logger.exception("__!Exception raised_")

    # WDW(browser, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "My Account"))).click()

    # WDW(browser, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()



@when("the user inputs valid <email> and <password>")
def input_credts(browser, email, password, report_logger):
    """
    Args:
        browser:
        email:
        password:
        report_logger:
    """
    assert "Login" in browser.page_source
    print >> sys.stderr, browser.current_url
    try:
        report_logger.info("Login authentication with "
                           "email: %s " % email + " password: %s" % password)
        elem = browser.find_element_by_xpath(ELEMENT_LOCATORS['login_email'])
        elem.send_keys(email)
        elem = browser.find_element_by_xpath(ELEMENT_LOCATORS['login_password'])
        report_logger.debug("%s elem", elem)
        elem.send_keys(password)

        elem.send_keys(Keys.RETURN)

    except Exception as e:
        report_logger.debug("Exception Raised ".format(e))

    report_logger.info("Current time : %s" % time.asctime(time.localtime()))
    time.sleep(PAGE_LOAD_WAIT)
    report_logger.info("we waited for 5 sec and now its : %s" % time.asctime(time.localtime()))
    # WDW(browser, PAGE_LOAD_WAIT).until(EC.url_changes(LOGIN_PAGE),browser.current_url)
    # time.sleep(2)
    report_logger.info("checking the url ...: %s" % browser.current_url)


@when('the user inputs incorrect email xor password')
def invalid_credts(browser, report_logger):
    """
    Args:
        browser:
        report_logger:
    """
    report_logger.info("___current title %s" % browser.title)
    report_logger.info("___current url %s" % browser.current_url)
    input_credts(browser, CREDENTIALS['invalid'].get('email'), CREDENTIALS['invalid'].get('password'), report_logger)
    assert "Login" in browser.title


# Then step definitions
@then('the web page reloads the login_page with a warning message')
def login_fails(browser, report_logger):
    """
    Args:
        browser:
        report_logger:
    """
    report_logger.warning("redirecting back to login page")
    report_logger.info("___current title %s" % browser.title)
    report_logger.info("___current url %s" % browser.current_url)
    assert "Login" in browser.title
    assert get_page_url('login_path') in browser.current_url
    # time.sleep(PAGE_LOAD_WAIT)
    assert "Invalid Email or Password" in browser.page_source


@then('the web page reloads successfully to the account_page')
def redirected_to_acc(browser, report_logger):
    """
    Args:
        browser:
        report_logger:
    """
    report_logger.info("___current title %s" % browser.title)
    report_logger.info("___current url %s" % browser.current_url)
    assert EC.title_contains("My Account")
    assert get_page_url('my_account_path') in browser.current_url


@when("the user selects the Logout option")
def logout(browser, report_logger):
    """
    Args:
        browser:
        report_logger:
    """
    try:  #/html/body/nav/div/div[2]/ul[2]/ul/li[1]/ul/li[2]/a
        browser.find_element_by_xpath(ELEMENT_LOCATORS['myaccount_dd_menu']).click()
        WDW(browser, PAGE_LOAD_WAIT).until(EC.element_to_be_clickable((By.XPATH, ELEMENT_LOCATORS['myaccount_dd_menu_item2']))).click()
        #time.sleep(PAGE_LOAD_WAIT)

    except Exception as e:
        report_logger.exception("EXCEPTION raised:".format(e))
    report_logger.info("___current title %s" % browser.title)
    report_logger.info("___current url %s" % browser.current_url)
    report_logger.warning("___logging out...")
    # report_logger.debug("elem : %s"% elem.text)


@then( "the user should not be able to access the account_page")
def logged_out(browser, report_logger):
    """
    Args:
        browser:
        report_logger:
    """
    report_logger.info("___current title %s" % browser.title)
    report_logger.info("___current url %s" % browser.current_url)

    req = request(browser)
    response = req.get(get_page_url('my_account_path'))
    report_logger.debug("_requested_status_code %d" % response.status_code)
    assert get_page_url('login_path') in browser.current_url


def request(driver):
    """
    Args:
        driver:
    """
    s = requests.Session()
    cookies = driver.get_cookies()
    for cookie in cookies:
        s.cookies.set(cookie['name'], cookie['value'])
    return s
