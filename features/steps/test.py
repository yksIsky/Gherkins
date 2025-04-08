from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://demoqa.com/")
x = driver.find_element(By.XPATH,"//div[@class='card-body']/h5[1]")

x.click()
driver.find_element(By.XPATH,"//*[@id='item-0']/span").click()
wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='userName-label']")))

print(driver.find_element(By.XPATH,"//*[@id='userName-label']").text)
assert driver.find_element(By.XPATH,"//*[@id='userName-label']").text == "Full Name"
#assert driver.find_element(By.XPATH,"//*[@id='userName-label']").get_attribute("value") == "Full Name"
#assert driver.find_element(By.XPATH,"//*[@id='userName-label']").get_attribute("href") == "Full Name"
#wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='genterWrapper']/div[2]/div[3]")))
