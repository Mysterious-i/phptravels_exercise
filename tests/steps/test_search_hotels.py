from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

from commons import get_page_url, PAGE_LOAD_WAIT

# Constants


# Scenarios

scenarios('../features/search_hotels.feature')

url_path = ""


@given(parsers.parse('I am an authenticated user in the {hotels_page}'))
def search(browser, hotels_page):
    """
    @scenario('login.feature')
    Args:
        browser (webdriver):
        hotels_page (str):

    Returns:

    """
    hotels_page = get_page_url('')
    return browser.get(hotels_page)


# TODO seperate the element locators
# TODO create a class for automating hotel input test data
@when("The user enters the query data <city>,<checkin_date>,<checkout_date>,<family_size>")
def search_inputs(browser, report_logger, city, checkin_date, checkout_date, family_size):
    """
    Args:
        browser ():
        report_logger:
        city:
        checkin_date:
        checkout_date:
        family_size:
    """
    search_inputs = {
        'city': city if city else "_blank_",
        'checkin': checkin_date if checkin_date else "_blank_",
        'checkout': checkout_date if checkout_date else "_blank_",
        'family_size': family_size if family_size else "_blank_"
    }
    # if city||
    fam_list = (family_size.partition('_'))

    num_adult = fam_list.__getitem__(0)
    num_adult = int(num_adult)
    num_child = fam_list.__getitem__(2)
    num_child = int(num_child)
    report_logger.info("__search query input data: " + search_inputs['city'] + "|" +
                       search_inputs['checkin'] + "|" +
                       search_inputs['checkout'] + "|" +
                       search_inputs['family_size'])
    report_logger.debug("city %d" % len(city))
    try:
        if city.strip():
            wait(browser, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Search by Hotel or City Name"))).click()
            wait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#select2-drop .select2-input"))).send_keys(
                city)
            wait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="select2-drop"]/ul/li/ul/li[1]'))).click()
        # elem = browser.find_element_by_xpath('//*[@id="s2id_autogen1"]#s2id_autogen1#select2-drop > div > input
        # report_logger.debug("city %s,"% city)
        report_logger.debug("stripping %s" % (checkin_date.strip('/')))

        wait(browser, PAGE_LOAD_WAIT).until(EC.element_to_be_clickable((By.NAME, 'checkin'))).send_keys(checkin_date)
        # browser.find_element_by_name('checkin').send_keys(checkin_date)
        # elem.send_keys(Keys.TAB)
        wait(browser, PAGE_LOAD_WAIT).until(EC.element_to_be_clickable((By.NAME, 'checkout'))).click()
        # browser.find_element_by_name('checkout').click()
        wait(browser, PAGE_LOAD_WAIT).until(EC.element_to_be_clickable((By.NAME, 'checkout'))).send_keys(checkout_date)
        # browser.find_element_by_name('checkout').send_keys(checkout_date)
        # elem.send_keys(Keys.TAB)
        # elem = browser.find_element_by_xpath('//*[@id="travellersInput"]').click()
        wait(browser, PAGE_LOAD_WAIT).until(EC.element_to_be_clickable((By.ID, 'travellersInput'))).click()

        # WDW(browser, PAGE_LOAD_WAIT).until(EC.element_to_be_selected((By.ID, "travellersInput"))).click()
        # time.sleep(2)
        report_logger.debug("__input data:adults :{:d}".format(int(num_adult)))
        a_add = num_adult - 2
        if a_add <= 0:
            iterations = -a_add
            for adults in range(iterations):
                wait(browser, PAGE_LOAD_WAIT).until(EC.element_to_be_clickable((By.ID, 'adultMinusBtn'))).click()
                # browser.find_element_by_id('adultMinusBtn').click()
        else:
            for adults in range(a_add):
                wait(browser, PAGE_LOAD_WAIT).until(EC.element_to_be_clickable((By.ID, 'adultPlusBtn'))).click()
                # browser.find_element_by_id('adultPlusBtn').click()
        for children in range(num_child):
            wait(browser, PAGE_LOAD_WAIT).until(EC.element_to_be_clickable((By.ID, 'childPlusBtn'))).click()
            # browser.find_element_by_id('childPlusBtn').click()

        wait(browser, PAGE_LOAD_WAIT).until(
            EC.text_to_be_present_in_element_value((By.ID, 'travellersInput'),
                                                   ("%d Adult " % num_adult + "%d Child" % num_child))
        )
        report_logger.warning("__url before search query %s" % browser.current_url)
        wait(browser, PAGE_LOAD_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))).click()
        # browser.find_element_by_xpath('//button[@type="submit"]').click()

        # time.sleep(5)
        global url_path
        search_url = "/" + city.strip() + \
                     "/" + checkin_date.replace('/', '-') + \
                     "/" + checkout_date.replace('/', '-') + \
                     "/%d" % num_adult + "/%d" % num_child
        report_logger.warning("__search url %s" % search_url)
        url_path = search_url  # type: str
        report_logger.info("___ext-url %s" % url_path)
        pass
    except Exception as e:
        report_logger.exception("___EXCEPTION raised:")


@then("The search results are displayed")
def display_results(browser):
    # pass
    """
    Args:
        browser:
    """
    wait(browser, PAGE_LOAD_WAIT).until(EC.url_contains("search"))
    assert "Search Results" in browser.page_source
    assert EC.url_contains(url_path)


# https://www.phptravels.net/hotels/search/france/paris/24-12-2018/25-12-2018/2/0
# https://www.phptravels.net/hotels/search/india/pune/01-01-2019/26-02-2019/2/0
@when(parsers.parse("The user enters {incomplete} data"))
def incomplete_search_input(browser, report_logger, incomplete):
    """
    Args:
        browser:
        report_logger:
        incomplete:
    """
    report_logger.warning("__incomplete...")
    search_inputs(browser, report_logger, "", "", "", "2_0")

    # raise NotImplementedError(u'STEP: When The user enters <incomplete> data')


@then("The web page reloads with a warning message on missing the data")
def alert_incomplete_data(browser, report_logger):
    """
    Args:
        browser:
        report_logger:
    """
    try:

        expectd_alert_text = "Please fill out this field."
        elem = browser.find_element_by_name('checkin')
        actual = elem.get_attribute('validationMessage')

        report_logger.warning("_actual alert text : %s" % actual)
        # C.move_to_element(elem)
        # wait(browser,PAGE_LOAD_WAIT).until(EC.text_to_be_present_in_element(By.NAME,"checkin"),"Please fill out this field")
        # report_logger.warning(expectd_alert_text)
        assert expectd_alert_text in actual
    except Exception as e:
        report_logger.exception("__couldnt find the alert box")
        raise Exception
    # pass

# raise NotImplementedError(u'STEP: Then The web page reloads with a warning message on missing the data')
