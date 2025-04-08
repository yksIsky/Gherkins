from behave import given, when, then

@given('I have username "user1" and password "pass123"')
def step_given_user_pass(context):
    context.username = "user1"
    context.password = "pass123"

@when("I log in")
def step_when_login(context):
    if context.username == "user1" and context.password == "pass123":
        context.message = f"Welcome {context.username}"
    else:
        context.message = "Login failed"

@then('I should see "Welcome user1"')
def step_then_see_message(context):
    assert context.message == "Welcome user1"

