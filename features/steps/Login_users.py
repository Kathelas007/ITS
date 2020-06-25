from behave import *

from common import *

import random


@given("Admin exists")
def step_impl(context):
    ...


@when("Admin logs in")
def step_impl(context):
    log_in_user(context, admin_user, admin_user)


@then("Log in succeeded")
def step_impl(context):
    driver = context.browse
    if 'dashboard' not in driver.current_url:
        time.sleep(1)

    if 'dashboard' in driver.current_url:
        my_log('log in succeeded FAILED ' + driver.current_url)

    assert "dashboard" in driver.current_url


@given("Enabled User exists")
def step_impl(context):
    ...


@when("Enabled User logs in")
def step_impl(context):
    log_in_user(context, enabled_user, enabled_user)


@when("Enabled User logs in with Admin password")
def step_impl(context):
    log_in_user(context, enabled_user, admin_user)


@then("Log in failed")
def step_impl(context):
    driver = context.browse

    if 'dashboard' in driver.current_url:
        time.sleep(0.5)

    if 'dashboard' in driver.current_url:
        my_log('log in failed FAILED ' + driver.current_url)

    assert "dashboard" not in driver.current_url


@when("Enabled User logs in with his password")
def step_impl(context):
    log_in_user(context, enabled_user, enabled_user)


@given("Users password is changed")
def step_impl(context):
    new_password = str(random.randint(0, 5000)) + "password"
    change_user_password(context, 5, new_password)


@when("User Logs in with old password")
def step_impl(context):
    # its not too fast, wait until the database process change
    time.sleep(2)
    log_in_user(context, basic_user, basic_user)


@given("Users user name is changed")
def step_impl(context):
    context.new_username = 'new nickname'
    change_user_name(context, 5, context.new_username)


@when("User Logs in with new user name")
def step_impl(context):
    # its not too fast, wait until the database process change
    time.sleep(2)
    log_in_user(context, context.new_username, basic_user)


@given("User is disabled")
def step_impl(context):
    ...


@when("Disabled User logs in")
def step_impl(context):
    log_in_user(context, disabled_user, disabled_user)


@given("Log in displayed")
def step_impl(context):
    driver = context.browse
    driver.get(pu_login)


@when("Fake User logs in")
def step_impl(context):
    log_in_user(context, fake_user, fake_user)


@given("Enabled User logs in with Admin password")
def step_impl(context):
    log_in_user(context, enabled_user, admin_user)
