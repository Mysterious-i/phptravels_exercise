import time

from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

# Constants


# Scenarios

scenarios('../features/search_hotels.feature')


# Fixtures

@given(parsers.parse('I am an authenticated user in the Home page$'))
def search(browser):
    browser.get('https://www.phptravels.net/m-hotels')
    pass


@when(parsers.parse('I search with inputing {city},{checkin_date},{checkout_date},{family_size}'))
def search_inputs(browser, city, checkin_date, checkout_date, family_size):
    # elem = browser.find_element_by_xpath('//*[@id="s2id_autogen1"]#s2id_autogen1#select2-drop > div > input

    wait(browser, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Search by Hotel or City Name"))).click()
    wait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#select2-drop .select2-input"))).send_keys(
        city)
    wait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="select2-drop"]/ul/li/ul/li[1]'))).click()
    elem = browser.find_element_by_name('checkin')
    elem.send_keys(checkin_date)
    elem.send_keys(Keys.TAB)
    elem = browser.find_element_by_name('checkout')
    elem.send_keys(checkout_date)
    elem.send_keys(Keys.TAB)
    elem = browser.find_element_by_xpath('//*[@id="travellersInput"]')
    elem.send_keys(family_size)
    elem.send_keys(Keys.RETURN)
    time.sleep(10)


@then("The search results are displayed")
def display_results(browser):
    assert "Search Results" in browser.page_source
