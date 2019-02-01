import sys
import time
import pytest
import requests
from pytest_bdd import scenarios, given, when, then
from selenium.common.exceptions import WebDriverException as driverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

from commons import get_page_url, PAGE_LOAD_WAIT, ELEMENT_LOCATORS, CREDENTIALS


scenarios('../features/password_recovery.feature')

data = {'valid': 'user@phptravels.com', 'valid_unregistered': 'a@b.c', 'invalid': 'bla'}


@pytest.fixture()
def input():
    data = {'valid': 'user@phptravels.com', 'valid_unregistered': 'a@b.c', 'invalid': 'bla'}
    return data


def reset_password(browser, report_logger, input_email):

    pass


@when('the user submits a reset_password request by inputing <input_email> email')
def successful_reset(browser, input_email, report_logger):
    # data.get(input_email)
    # report_logger.war
    report_logger.info("___current title %s" % browser.title)
    report_logger.info("___current url %s" % browser.current_url)
    report_logger.info("__locating the reset password button...")
    try:
        # xpath : //*[@id="loginfrm"]/div[2]/div[3]/a
        # "//a[contains(@href,'text')]"
        # css :#loginfrm > div.wow.zoomInDown.animated.row.animated > div:nth-child(3) > a
        elem = browser.find_element_by_xpath(ELEMENT_LOCATORS["//a[contains(@href,'text')]"])
        report_logger.warning(elem.text)
        #elem.send_keys(email)
        # WDW(browser, PAGE_LOAD_WAIT).until(
        #     EC.element_to_be_clickable((By.XPATH, ELEMENT_LOCATORS["//a[contains(@href,'text')]"]))).click()
        # WDW(browser, PAGE_LOAD_WAIT).until(
        #     EC.element_to_be_clickable((By.XPATH, ELEMENT_LOCATORS['myaccount_dd_menu_item1']))).click()
        browser.implicitly_wait(PAGE_LOAD_WAIT)

    except driverException:
        report_logger.exception("__!Exception raised_")
    # raise NotImplementedError(u'STEP: When  the user submits a reset_password request by providing a valid_email')


@when("the user submits a reset_password request by providing an invalid_email")
def step_impl():
    raise NotImplementedError(u'STEP: When  the user submits a reset_password request by providing an invalid_email')


@when("the user submits a reset_password request by providing a valid_unregistered_email")
def step_impl():
    raise NotImplementedError(
        u'STEP: When  the user submits a reset_password request by providing a valid_unregistered_email')


@then("the web page alerts the user with the successful_password_reset message")
def step_impl():
    pass
    #raise NotImplementedError(u'STEP: Then  the web page alerts the user with the successful_password_reset message')


@then("the web page alerts the user with the email_not_found message")
def step_impl():
    raise NotImplementedError(u'STEP: Then  the web page alerts the user with the email_not_found message')


@then("the web page alerts the user with a warning message")
def step_impl():
    raise NotImplementedError(u'STEP: Then  the web page alerts the user with a warning message')


@then('the web page alerts the user with the "([^"]+)" message')
def step_impl():
    raise NotImplementedError(u'STEP: Then  the web page alerts the user with the "successful_password_reset" message')


@then('the web page alerts the user with the "successful_password_reset" message')
def step_impl():
    raise NotImplementedError(u'STEP: Then  the web page alerts the user with the "successful_password_reset" message')
