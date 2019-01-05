"""
This module contains shared fixtures, steps, and hooks.
"""
import os.path

import pytest
from selenium import webdriver

HOME_PAGE = 'https://www.phptravels.net'


def pytest_report_header(config):
    return "project deps: mylib-1.1"


@pytest.fixture
def browser():
    b = webdriver.Firefox()
    b.implicitly_wait(20)
    yield b
    b.quit()


# service_args=["--verbose", "--log-path=D:\\qc1.log"]


@pytest.fixture(scope='function')
def home_page(browser):
    """

    :param url_page: appending the page url to the home page
    :type browser: webdriver
    """
    return browser.get(HOME_PAGE)


# copied segment from https://docs.pytest.org/en/latest/example/simple.html
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # we only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""

            f.write(rep.nodeid + extra + "\n")


@pytest.fixture
def something(request):
    yield
    # request.node is an "item" because we use the default
    # "function" scope
    if request.node.rep_setup.failed:
        print("setting up a test failed!", request.node.nodeid)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            print("executing test failed", request.node.nodeid)
