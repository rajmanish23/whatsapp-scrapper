import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

group_name = "MREC III CSE C 2020"

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
driver.implicitly_wait(5)

WebDriverWait(driver, 60).until(
    ec.presence_of_element_located(
        (By.CLASS_NAME, '_3sHED')
    )
)

time.sleep(2)
input_box_search = driver.find_element(By.CLASS_NAME, 'to2l77zo')
input_box_search.click()
time.sleep(2)
input_box_search.send_keys(group_name)
time.sleep(2)

contact_element = driver.find_element(By.CLASS_NAME, "_8nE1Y")
contact_element.click()

input()
