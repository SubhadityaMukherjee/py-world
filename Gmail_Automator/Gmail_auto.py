def check_user_and_continue():
	data = open('data.txt','a+')
	data.seek(0)
	if(len(data.read())==0):
		data.write(input("Enter username: ")+'\n')
		data.write(input("Enter password: ")+'\n')
		data.close()
	else:
		mainprog()

def mainprog():
	from selenium import webdriver
	import time
	from selenium.webdriver.common.keys import Keys
	data = open('data.txt','r')
	uspass = data.readlines()

	a = input("Enter email address(multiple separated by comma: ")
	s = input("Enter subject: ")
	t = input("Enter text: ")


	browser = webdriver.Chrome()
	browser.get('https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=AddSession')

	userid = browser.find_element_by_name("identifier")
	userid.send_keys(uspass[0].rstrip())
	userid.send_keys(u'\ue007')

	time.sleep(2)

	passw = browser.find_element_by_name("password")
	passw.send_keys(uspass[1].rstrip())
	passw.send_keys(u'\ue007')

	time.sleep(10)

	browser.get('https://mail.google.com/mail/u/0/#inbox?compose=new')

	time.sleep(5)

	to = browser.find_element_by_name("to")
	to.send_keys(a)
	to.send_keys(Keys.RETURN)
	fr = browser.find_element_by_name("subjectbox")
	fr.send_keys(s)
	fr.send_keys(Keys.RETURN)
	fr.send_keys(Keys.TAB)

	x = browser.switch_to.active_element
	time.sleep(1)
	x.send_keys(t)
	time.sleep(2)
	x.send_keys(Keys.TAB)
	z =browser.switch_to.active_element
	z.click()

	if(len(input("click return to exit"))>=0):
		exit()

check_user_and_continue()
