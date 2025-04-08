from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('I have username "user1" and password "pass123"')
def step_given_user_pass(context):
    context.username = "user1"
    context.password = "pass123"
    # Inicjalizacja drivera
    context.driver = webdriver.Chrome()
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

    # Poczekaj aż będzie klikalny i kliknij przez JS (ze względu na reklamy)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='card-body']/h5[1]")))
    driver.execute_script("arguments[0].click();", element)

    # Kliknij na "Text Box"
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='item-0']/span"))).click()

    # Poczekaj aż pojawi się etykieta "Full Name"
    label = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='userName-label']")))

    print(label.text)
    assert label.text == "Full Name"

    driver.quit()
