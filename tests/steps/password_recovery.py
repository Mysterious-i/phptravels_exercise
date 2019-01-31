from pytest_bdd import scenarios, given, when, then, parsers
import pytest

scenarios('../features/search_hotels.feature')

data = {'valid': 'user@phptravels.com', 'valid_unregistered': 'a@b.c', 'invalid': 'bla'}


@pytest.fixture()
def input():
    data = {'valid': 'user@phptravels.com', 'valid_unregistered': 'a@b.c', 'invalid': 'bla'}
    return data


def reset_password(browser, report_logger, input_email):
    pass


@when('the user submits a reset_password request by inputing <input_email> email')
def step_impl(browser, input_email, report_logger):
    # data.get(input_email)
    # report_logger.war

    raise NotImplementedError(u'STEP: When  the user submits a reset_password request by providing a valid_email')


@when("the user submits a reset_password request by providing an invalid_email")
def step_impl():
    raise NotImplementedError(u'STEP: When  the user submits a reset_password request by providing an invalid_email')


@when("the user submits a reset_password request by providing a valid_unregistered_email")
def step_impl():
    raise NotImplementedError(
        u'STEP: When  the user submits a reset_password request by providing a valid_unregistered_email')


@then("the web page alerts the user with the successful_password_reset message")
def step_impl():
    raise NotImplementedError(u'STEP: Then  the web page alerts the user with the successful_password_reset message')


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
