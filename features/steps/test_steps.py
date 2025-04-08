from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I have username "user1" and password "pass123"')
def step_given_user_pass(context):
    options = Options()
    options.add_argument("--headless")  # tryb bez GUI
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    context.driver = webdriver.Chrome(options=options)
    context.username = "user1"
    context.password = "pass123"
    context.wait = WebDriverWait(context.driver, 10)

@when("I log in")
def step_when_login(context):
    if context.username == "user1" and context.password == "pass123":
        context.message = f"Welcome {context.username}"
    else:
        context.message = "Login failed"

@then('I should see "Welcome user1"')
def step_then_see_message(context):
    assert context.message == "Welcome user1"
    driver = context.driver
    wait = context.wait

    driver.get("https://demoqa.com/")
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='card-body']/h5[1]")))
    driver.execute_script("arguments[0].click();", element)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='item-0']/span"))).click()

    label = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='userName-label']")))
    assert label.text == "Full Name"
