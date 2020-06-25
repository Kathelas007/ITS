import selenium
import unittest, time, re

# WebDriver
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from selenium import webdriver  # or any custom webdriver
from behave.model import Feature

from common import *

logging_feature = ['Navigation and functionality of Users page', 'Navigation and functionality of Add Users page',
                   'Navigation and functionality of Edit User page', 'Log in User in different states']


def before_feature(context, feature: Feature):
    global logging_feature
    if feature.name in logging_feature:  # and feature.name == 'Navigation and functionality of Edit User page':
        log_in_user(context, 'admin', 'admin')
        display_user_page(context)

    if feature.name == 'Log in User in different states':
        all_users = get_all_user_nicknames(context)
        # sort if needed
        if not all_users[0].lower().startswith('a'):
            click_button_xpath(context, '//*[@id="form-user"]/div/table/thead/tr/td[2]/a')


def after_feature(context, feature):
    global logging_feature
    if feature.name in logging_feature:  # and feature.name == 'Navigation and functionality of Edit User page':
        log_out(context)

    time.sleep(0.4)


def after_scenario(context, scenario):
    to_list_scen = ['Nothing filled out', 'One obligatory row missing', 'Wrong Password Confirm', 'Same User Name',
                    'Add User', 'Edit User']

    sc_name = scenario.name.split(" -- @")[0]

    if sc_name in to_list_scen:
        time.sleep(0.2)
        click_cancel(context)
        time.sleep(0.2)

    if sc_name == 'User Logs in with old password':
        change_user_password(context, 5, basic_user)

    if sc_name == 'User Logs in with new user name':
        change_user_name(context, 5, basic_user)


def before_all(context):
    # context.browse = webdriver.Firefox()

    context.browse = webdriver.Remote(
        command_executor='http://mys01.fit.vutbr.cz:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)

    context.default_wait = 3
    context.browse.implicitly_wait(context.default_wait)


def after_all(context):
    context.browse.quit()
