import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

group_name = "COPIUM LAN"  # enter group name
refresh_time_in_min = 10  # enter in minutes

refresh_time = refresh_time_in_min * 60

URL_REGEX = r"https://us04web.zoom.us/j/.+?\b"
WELCOME_ART_CLASS = '_3sHED'
SEARCH_BOX_CLASS = 'to2l77zo'
GROUP_CLASS = "_8nE1Y"
LAUNCH_MEETING_BTN_CLASS = "mbTuDeF1"
MESSAGE_CLASS = "_11JPr"

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
driver.implicitly_wait(5)

original_window = driver.current_window_handle

WebDriverWait(driver, 60).until(
    ec.presence_of_element_located(
        (By.CLASS_NAME, WELCOME_ART_CLASS)
    )
)

time.sleep(2)
input_box_search = driver.find_element(By.CLASS_NAME, SEARCH_BOX_CLASS)
input_box_search.click()
input_box_search.send_keys(group_name)
time.sleep(2)

contact_element = driver.find_element(By.CLASS_NAME, GROUP_CLASS)
contact_element.click()

time.sleep(2)


def open_link(latest_link_f):
    driver.switch_to.new_window('tab')
    driver.get(latest_link_f)

    WebDriverWait(driver, 20).until(
        ec.presence_of_element_located(
            (By.CLASS_NAME, LAUNCH_MEETING_BTN_CLASS)
        )
    )
    launch_meeting_btn = driver.find_element(By.CLASS_NAME, LAUNCH_MEETING_BTN_CLASS)
    launch_meeting_btn.click()

    time.sleep(5)
    driver.close()
    driver.switch_to.window(original_window)


current_link = ""
while True:
    message_elements = driver.find_elements(By.CLASS_NAME, MESSAGE_CLASS)
    latest_link = message_elements[-1].text
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(f"{current_time} : {latest_link}")

    url_match = re.search(URL_REGEX, latest_link)

    if latest_link != current_link and url_match is not None:
        current_link = latest_link
        open_link(latest_link)
    else:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(f"{current_time} : Link is same. Not opened")

    time.sleep(refresh_time)
