from behave import given, when, then, step

from common import *

import datetime


@given('"Users" displayed')
def step_impl(context):
    assert check_subheader(context, sh_user_list)


@when("Sort by '{sort}'")
def step_impl(context, sort):
    sort_dic_index = {'Username': 2, 'Status': 3, 'Date Added': 4}
    click_button_xpath(context, f'//*[@id="form-user"]/div/table/thead/tr/td[{sort_dic_index[sort]}]/a')

    context.sort_index = sort_dic_index[sort]


@then("Users sorted by '{sort}'")
def step_impl(context, sort):
    all_data = []
    i = 1

    time.sleep(0.2)
    context.browse.implicitly_wait(1)
    while True:
        current = get_data_from_user_list(context, context.sort_index, i)
        if not current: break
        i = i + 1
        all_data.append(current)
    context.browse.implicitly_wait(context.default_wait)

    if context.sort_index == 4:
        for i, it in enumerate(all_data):
            date = it.split('/')
            all_data[i] = ''.join(date[::-1])

    elif context.sort_index == 2:
        all_data = [d.lower() for d in all_data]

    assert all_data == sorted(all_data) or all_data == sorted(all_data, reverse=True)


@when('"Add new" clicked')
def step_impl(context):
    click_add(context)


@then('"Edit User" displayed')
def step_impl(context):
    check_subheader(context, sh_edit_user)


@when("User is selected")
def step_impl(context):
    ...


@when("All Users selected")
def step_impl(context):
    time.sleep(0.4)
    click_button_xpath(context, '//*[@id="form-user"]/div/table/thead/tr/td[1]/input')
    context.users_in_list = get_all_user_nicknames(context)


@step("All Users Displayed")
def step_impl(context):
    assert context.users_in_list == get_all_user_nicknames(context)


@when('"Edit" clicked')
def step_impl(context):
    click_edit_user(context)


@then('"Users" displayed')
def step_impl(context):
    check_subheader(context, sh_user_list)


@when('"Delete" clicked')
def step_impl(context):
    click_delete(context)
