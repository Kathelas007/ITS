from behave import *

from behave import given, when, then, step

from common import *


@given('"Add User" displayed')
def step_impl(context):
    click_add(context)
    assert True is check_subheader(context, sh_add_user)


@when("Nothing filled out")
def step_impl(context):
    ...


@step("Save")
def step_impl(context):
    click_save(context)


@when("Cancel")
def step_impl(context):
    click_cancel(context)


@then("Users still displayed")
def step_impl(context):
    assert True is check_subheader(context, sh_user_list)


@step("All obligatory filled out")
def step_impl(context):
    assert check_subheader(context, sh_add_user) or check_subheader(context, sh_edit_user)
    fill_all_obligatory(context)


@when("Cleared one '{Obligatory}'")
def step_impl(context, Obligatory):
    field = Obligatory.split(' ')[0].lower()

    for obl in obligatory:
        if field in obl:
            field = obl
            break

    clear_row(context, field)


@when("'{Password}' and '{Confirm}' filled out")
def step_impl(context, Password, Confirm):
    clear_row(context, obligatory[3])
    fill_row(context, obligatory[3], Password)

    clear_row(context, obligatory[4])
    fill_row(context, obligatory[4], Confirm)


@given('User with "nickname" exists')
def step_impl(context):
    nickname = get_user_nickname_from_user_list(context)
    assert nickname
    context.nickname = nickname


@when('Create another User with "nickname"')
def step_impl(context):
    fill_all_obligatory(context)
    clear_row(context, obligatory[0])
    clear_row(context, obligatory[3])
    clear_row(context, obligatory[4])

    context.password = 'my secret password'
    fill_row(context, obligatory[0], context.nickname)
    fill_row(context, obligatory[3], context.password)
    fill_row(context, obligatory[4], context.password)

    click_save(context)


@then('"Add User" displayed')
def step_impl(context):
    assert check_subheader(context, sh_add_user)
