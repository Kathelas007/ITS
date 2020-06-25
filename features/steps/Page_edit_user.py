from behave import given, when, then, step

from common import *


@when('User\'s "Username" changed')
def step_impl(context):
    click_edit_user(context)
    origo_nickname = get_row(context, obligatory[0])
    if origo_nickname != "AAA nickname":
        new_nickname = "AAA nickname"
    else:
        new_nickname = "AAA NICKNAME"

    clear_row(context, obligatory[0])
    fill_row(context, obligatory[0], new_nickname)
    click_save(context)

    context.origo_nickname = origo_nickname
    context.new_nickname = new_nickname


@then('New "Username" displayed')
def step_impl(context):
    assert check_subheader(context, sh_user_list)

    all_users = get_all_user_nicknames(context)
    assert context.new_nickname in all_users


@when("User's '{info}' changed")
def step_impl(context, info):
    click_edit_user(context)

    if info.lower().startswith('first'):
        info = obligatory[1]
    else:
        info = obligatory[2]

    info_text = get_row(context, info)

    clear_row(context, info)

    if info_text != "Lila":
        fill_row(context, info, 'Bendr')
    else:
        fill_row(context, info, "Lila")

    click_save(context)


@when('User\'s "State" changed')
def step_impl(context):
    click_edit_user(context)

    curr_status = get_status(context)

    if curr_status == st_disabled:
        new_status = st_enabled
    else:
        new_status = st_disabled

    set_status(context, new_status)
    click_save(context)

    context.curr_state = new_status


@then('New "State" displayed')
def step_impl(context):
    assert check_subheader(context, sh_user_list)

    curr_state = get_data_from_user_list(context, 3)
    assert curr_state == context.curr_state
