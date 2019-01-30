from typing import Dict

PATHS = {
    'home': "/en",
    'search_hotels_path': "/m-hotels",
    'login_path': "/login",
    'logout_path': "/logout",
    'my_account_path': "/account"
}  # type: Dict[str, str]
HOME_PAGE = "https://www.phptravels.net"
PAGE_LOAD_WAIT = 3

ELEMENT_LOCATORS = {

    'login_email': "//input[@name='username']",
    'login_password': "//input[@name='password']",
    'menu': "dropdown-toggle go-text-right",
    'myaccount_dd_menu':"/html/body/nav/div/div[2]/ul[2]/ul/li[1]/a",
    'myaccount_dd_menu_item1':'/html/body/nav/div/div[2]/ul[2]/ul/li[1]/ul/li[1]',
    'myaccount_dd_menu_item2':'/html/body/nav/div/div[2]/ul[2]/ul/li[1]/ul/li[2]',
    'my_account_dropdown': "//nav[contains(@class,'navbar-default')]//li[@id='li_myaccount']"
                           "//a[contains(@class,'dropdown-toggle')]",
    'logout_dropdown': "body > nav > div > div.collapse.navbar-collapse > "
                       "ul.nav.navbar-nav.navbar-right.hidden-sm.go-left > ul > li:nth-child(1) > a"

}
CREDENTIALS = {
    'valid': {'email': "user@phptravels.com",
              'password': "demouser"},
    'invalid': {'email': " ",
                'password': "demouser"}
}  # type: Dict[('valid or invalid'):str, Dict['email':str, 'password':str]]


def get_page_url(path):
    if PATHS.has_key(path):
        req_page_url = HOME_PAGE + PATHS[path]
        return req_page_url
    else:
        return HOME_PAGE
