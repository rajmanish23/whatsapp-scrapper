import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as ec

group_name = "COPIUM LAN"

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
driver.implicitly_wait(5)

original_window = driver.current_window_handle

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

time.sleep(2)


def open_link():
    message_elements = driver.find_elements(By.CLASS_NAME, "_11JPr")
    latest_message = message_elements[-1].text
    print(latest_message)

    driver.switch_to.new_window('tab')
    driver.get(latest_message)

    time.sleep(5)
    launch_meeting_btn = driver.find_element(By.CLASS_NAME, "mbTuDeF1")
    launch_meeting_btn.click()

    time.sleep(20)
    driver.switch_to.window(original_window)



for i in range(2):
    open_link()

input()
