"""
This module contains shared fixtures, steps, and hooks.
"""
import pytest
import logging
import logging.config
import os.path
import sys
import time
from logging import Logger
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

t = time.localtime()
TIME_STAMP = "%s___" % time.asctime(t)
# some Data
default_html_report_name = "report_" + time.strftime("%b%d_%H-%M", t) + ".html"


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    html_reports_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                             '..', '.html_reports')
    try:
        os.mkdir(html_reports_dir)
    except OSError as e:
        pass
    html_report_path = os.path.join(html_reports_dir,default_html_report_name)
    if not config.option.htmlpath:
        if os.path.exists(html_reports_dir):
            config.option.htmlpath = html_report_path
        else:
            config.option.htmlpath = default_html_report_name


# TODO:  modify code to reflect the use of this fixture once per session
@pytest.fixture()
def browser(report_logger):
    # For now only testing with the Firefox webdriver

    # TODO: test with Chrome and Safari drivers
    """
    Args:
        report_logger (logging.Logger)
    """
    opties = Options()
    opties.log.level = 'trace'
    driver = webdriver.Firefox(options=opties)

    # report_logger.info(driver.get_log('browser'))
    # report_logger.addHandler(logging.FileHandler('logsss.log','a'))
    # logger.info("accessing log types %s"% driver.log_types)
    # executor_url = driver.command_executor._url
    session_id = driver.session_id
    report_logger.info("___current session id %s___" % session_id)
    # logs = webdriver.firefox.options.Log

    # report_logger.info("driverlogs type {}".format(logs))
    # driver.implicitly_wait(20)
    yield driver
    driver.delete_all_cookies()
    driver.quit()


# service_args=["--verbose", "--log-path=D:\\qc1.log"]


@pytest.fixture()
def report_logger():
    logger = logging.getLogger(__name__)  # type: Logger
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('report_log.log', 'a')
    fh.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - (logged from %(filename)s:%(funcName)s:%(lineno)s) -'
                                  ' %(name)s - %(levelname)s - %(message)s -')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # Add the Handler to the Logger
    logger.addHandler(ch)
    logger.addHandler(fh)
    logger.info('__Finished setting up the logger at %s' % TIME_STAMP)
    # logger.info('logger type {}'.format(type(logger)))
    return logger

@pytest.hookimpl
def pytest_bdd_apply_tag(tag, function):
    if tag == 'todo':
        marker = pytest.mark.skip(reason="Not implemented yet")
        marker(function)
        return True
    else:
        # Fall back to pytest-bdd's default behavior
        return None

@pytest.hookimpl
def pytest_bdd_before_step(request, feature, scenario, step, step_func):
    logger = logging.getLogger(__name__)
    logger.info(("**{}**".format(step)))

@pytest.hookimpl(hookwrapper=True)
def pytest_sessionfinish(exitstatus):
    outcome = yield
    rep = outcome.get_result()
    # print >> sys.stdout, "rep from session finish %s\n" % rep
    cache_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                             '..', '.cache')
    try:
        os.mkdir(cache_dir)
    except OSError as e:
        pass

    status_file = os.path.join(cache_dir, 'pytest_status')
    mode = "a" if os.path.exists(".cache/pytest_status") else "w"
    with open(status_file, mode) as f:
        report = time.asctime(time.localtime()) + "__exitstatus__" + str(exitstatus) + '\n'
        f.write(report)


# copied segment from https://docs.pytest.org/en/latest/example/simple.html
@pytest.hookimpl(trylast=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    global default_html_report_name
    rep = outcome.get_result()
    setattr(item, "REPORT_" + rep.when, rep)
    # we only look at actual test calls, not setup/teardown
    if rep.when == "call":
        mode = "a" if os.path.exists("runs.txt") else "w"
        with open("runs.txt", mode) as f:
            # let's also access a fixture for the fun of it

            # let's also access a fixture for the fun of it
            # if "tmpdir" in item.fixturenames:
            #     extra = "HI(%s)" % item.funcargs["tmpdir"]
            # else:
            #     extra = "what"

            # f.write(rep.nodeid + extra + "\n")

            f.write(TIME_STAMP + rep.nodeid + "\n")
