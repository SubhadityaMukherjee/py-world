from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def hx(n):
	s=''
	for a in n:
		s+=(chr(ord(a)+40)+'/')
	return(s)

def unhx(z):
	n=z.split('/')
	s=''
	for a in n:
		if len(a)>0:
			s+=(chr(ord(a)-40))
	return(s)

def addlogin():
	data = open('data.txt','a+')
	data.seek(0)
	a = input('Enter username: ')
	b = input('Enter password: ')
	data.write(hx(a)+'\n')
	data.write(hx(b)+'\n')
	data.close()
def loginto():
	data = open('data.txt','r')
	data.seek(0)
	chrome_options = Options()
	chrome_options.add_argument("--headless") 
	browser = webdriver.Chrome(chrome_options=chrome_options)
	browser.get('http://phc.prontonetworks.com/cgi-bin/authlogout?URI=http://phc.prontonetworks.com/')
	browser.get('http://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://www.msftconnecttest.com/redirect')
	data.seek(0)
	x = data.readlines()
	try:
		userid = browser.find_element_by_name("userId")
		userid.send_keys(unhx(x[0]))
		password = browser.find_element_by_name("password")
		password.send_keys(unhx(x[1]))
		submit = browser.find_element_by_name("Submit22")
		submit.click()
		print('Logged into',unhx(x[0]))
	except:
		try:
			userid = browser.find_element_by_name("userId")
			userid.send_keys(unhx(x[2]))
			password = browser.find_element_by_name("password")
			password.send_keys(inhx(x[3]))
			submit = browser.find_element_by_name("Submit22")
			submit.click()
			print('Logged into',unhx(x[2]))
		except:
			userid = browser.find_element_by_name("userId")
			userid.send_keys(unhx(x[4]))
			password = browser.find_element_by_name("password")
			password.send_keys(inhx(x[5]))
			submit = browser.find_element_by_name("Submit22")
			submit.click()
			print('Logged into',unhx(x[4]))
			
	
i = input("To add login type anything and hit enter. To logout type l and hit enter. To login hit enter ")
if len(i)>0:
	addlogin()
elif i.lower()=='l':
	browser.get('http://phc.prontonetworks.com/cgi-bin/authlogout?URI=http://phc.prontonetworks.com/')
else:
	loginto()		
	
