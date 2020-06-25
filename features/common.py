from selenium import webdriver  # or any custom webdriver
from behave.model import Feature
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException as TE
from selenium.common.exceptions import UnexpectedAlertPresentException as AE
from selenium.common.exceptions import WebDriverException as WE

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

import time
import random

"""  Login_users.feature:30  User Logs in with old password
  Login_users.feature:35  User Logs in with new user name
  Page_add_user.feature:41  Wrong Password Confirm -- @1.2 
  Page_add_user.feature:42  Wrong Password Confirm -- @1.3 
  Page_add_user.feature:44  Same User Name
"""


def my_log(msg):
    with open('./log.txt', 'a') as o:
        o.write(msg + "\n")


sh_user_list = 'User List'
sh_add_user = 'Add User'
sh_edit_user = 'Edit User'
sh_dashboard = 'Dashboard'

"""
Checking current User page
"""


def check_subheader(context, subheader):
    driver = context.browse

    wait = WebDriverWait(driver, 2)
    try:
        res = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h3'), subheader))
    except TE:
        res = False

    return res


"""
Clicking buttons
"""


def click_button_xpath(context, xpath):
    driver = context.browse
    chain = ActionChains(driver)

    wait = WebDriverWait(driver, 4)
    wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    new_button = driver.find_element_by_xpath(xpath)

    try:
        chain.click(new_button).perform()
    except AE:
        driver = context.browse
        driver.switch_to.alert.accept()


def click_edit_user(context, user=1):
    xpath = f'//*[@id="form-user"]/div/table/tbody/tr[{user}]/td[5]/a'
    click_button_xpath(context, xpath)


def click_cancel(context):
    click_button_xpath(context, '//*[@id="content"]/div[1]/div/div/a')


def click_save(context):
    click_button_xpath(context, '//*[@id="content"]/div[1]/div/div/button')


def click_add(context):
    click_button_xpath(context, '//*[@id="content"]/div[1]/div/div/a')


def click_delete(context):
    driver = context.browse
    chain = ActionChains(driver)

    wait = WebDriverWait(driver, 4)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[1]/div/div/button')))
    new_button = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/button')

    chain.click(new_button).perform()

    driver = context.browse
    driver.switch_to.alert.accept()


"""
Function operating in User page
"""


def get_data_from_user_list(context, d_type=2, number=1):
    driver = context.browse
    try:
        elem = driver.find_element_by_xpath(f'//*[@id="form-user"]/div/table/tbody/tr[{number}]/td[{d_type}]')
    except WE:
        return False

    return elem.text


def get_user_nickname_from_user_list(context, user=1):
    assert check_subheader(context, sh_user_list)
    return get_data_from_user_list(context, 2, user)


def get_all_user_nicknames(context):
    assert check_subheader(context, sh_user_list)

    context.browse.implicitly_wait(1)
    users = []

    current = True
    i = 1
    while current:
        current = get_user_nickname_from_user_list(context, i)
        users.append(current)
        i = i + 1

    context.browse.implicitly_wait(context.default_wait)
    return users


"""
Functions operating in Edit User page
"""

obligatory = ['input-username', 'input-firstname', 'input-lastname', 'input-password', 'input-confirm']


def fill_row(context, id, text):
    elem = context.browse.find_element_by_css_selector(f"[id={id}]")
    elem.send_keys(text)


def get_row(context, id):
    return context.browse.find_element_by_css_selector(f"[id={id}]").text


def clear_row(context, id):
    context.browse.find_element_by_css_selector(f"[id={id}]").clear()


def fill_all_obligatory(context):
    global obligatory
    for obl in obligatory:
        fill_row(context, obl, obl)


st_enabled = 'Enabled'
st_disabled = 'Disabled'


def get_status(context):
    status_select = Select(context.browse.find_element_by_css_selector("[id=input-status]"))
    curr_status = status_select.first_selected_option

    return curr_status.text


def set_status(context, state):
    status_select = Select(context.browse.find_element_by_css_selector("[id=input-status]"))
    status_select.select_by_visible_text(state)

    # workaround, selenium is not able to click upper buttons or scroll to them
    context.browse.find_element_by_css_selector('h1').click()


"""
Logging in / out
"""
xpl_user_name = '//*[@id="input-username"]'
xpl_password = '//*[@id="input-password"]'

pu_login = "http://pat.fit.vutbr.cz:8076/admin/"


def log_in_user(context, name, password):
    driver = context.browse
    driver.get(pu_login)

    elem = driver.find_element_by_xpath(xpl_user_name)
    elem.send_keys(name)

    elem = driver.find_element_by_xpath(xpl_password)
    elem.send_keys(password)

    elem.send_keys(Keys.ENTER)

    wait = WebDriverWait(driver, 3)

    try:
        wait.until(EC.url_contains('dashboard'))
    except TE:
        return False

    return True


def log_out(context):
    driver = context.browse

    try:
        click_button_xpath(context, '//*[@id="header"]/ul/li[4]/a')
    except:
        return False

    wait = WebDriverWait(driver, 3)

    try:
        wait.until(EC.url_contains('login'))
    except TE:
        return False
    return True


"""
Change some user info
"""

admin_user = 'admin'
enabled_user = 'enabled user'
disabled_user = 'disabled user'
basic_user = 'user'
fake_user = 'fake uuuuuuuuuuser'


def change_user_password(context, user_num, password):
    log_in_user(context, admin_user, admin_user)
    display_user_page(context)

    click_edit_user(context, user_num)

    fill_row(context, obligatory[3], password)
    fill_row(context, obligatory[4], password)

    click_save(context)
    log_out(context)


def change_user_name(context, user_num, user_name):
    log_in_user(context, admin_user, admin_user)
    display_user_page(context)
    click_edit_user(context, user_num)

    clear_row(context, obligatory[0])
    fill_row(context, obligatory[0], user_name)

    click_save(context)
    log_out(context)


def display_user_page(context):
    """
    Used after log in, navigate to User
    """
    driver = context.browse

    wait = WebDriverWait(driver, 4)

    actions = ActionChains(driver)
    system_el = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="system"]')))
    actions.click(system_el).perform()

    actions = ActionChains(driver)
    user_el = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/nav/ul/li[8]/ul/li[2]/a')))
    actions.click(user_el).perform()

    actions = ActionChains(driver)
    users2_elem = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="system"]/ul/li[2]/ul/li[1]/a')))
    actions.click(users2_elem).perform()

    assert True is check_subheader(context, sh_user_list)
