#import libs
from selenium import webdriver
import time
import selenium
from selenium.webdriver.common.keys import Keys

#function to close any other tabs other than 9anime.to
def close_Tab():
    windows = brower.window_handles
    if len(windows) > 1:
        brower.switch_to.window(windows[1])
        brower.close()
        print("Child window closed")
        brower.switch_to.window(windows[0])

#define username and password
username = "****"
password = "********"

#click sign in button 
def click():
    try:
        sign_in = brower.find_element_by_css_selector(
            "div.btn.btn-primary").click()
    except selenium.common.exceptions.NoSuchElementException:
        print("No element found")

#initialise browser and open 9anime.to
brower = webdriver.Chrome()
brower.get("https://9anime.to")

#let code wait 5 second
brower.implicitly_wait(5)

#call functions
click()
close_Tab()

#let code wait 3 second
brower.implicitly_wait(3)

#find username_textbox and password_textbox and send keys to it 
username_textbox = brower.find_element_by_xpath("//input[@placeholder=\'Username or email\']")
username_textbox.send_keys(username)

password_textbox = brower.find_element_by_xpath("//input[@placeholder=\'Password\']")
password_textbox.send_keys(password)

#click submit button 
password_textbox.submit()

#while loop to not let another tab open 
while True:
    close_Tab()
    time.sleep(2)