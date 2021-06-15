from selenium import webdriver
import time
import selenium
from selenium.webdriver.common.keys import Keys


def close_Tab():
    windows = brower.window_handles
    if len(windows) > 1:
        brower.switch_to.window(windows[1])
        brower.close()
        print("Child window closed")
        brower.switch_to.window(windows[0])


username = "cyrof"
password = "B@sketba1l"
counter = 0


def click():
    try:
        sign_in = brower.find_element_by_css_selector(
            "div.btn.btn-primary").click()
    except selenium.common.exceptions.NoSuchElementException:
        print("No element found")


brower = webdriver.Chrome()

brower.get("https://9anime.to")

brower.implicitly_wait(5)

click()

close_Tab()

brower.implicitly_wait(3)
username_textbox = brower.find_element_by_xpath("//input[@placeholder=\'Username or email\']")
username_textbox.send_keys(username)

password_textbox = brower.find_element_by_xpath("//input[@placeholder=\'Password\']")
password_textbox.send_keys(password)

password_textbox.submit()

while True:
    close_Tab()
    time.sleep(2)