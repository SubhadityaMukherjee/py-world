import time,os
class Diary:
	def __init__(self):
		self.f = open(time.strftime('%h'+'-' +'%m'+'-'+'%y')+'.txt','a+')
	def deco(self):
		self.f.write(time.strftime('%h'+' ' +'%m'+' '+'%y')+'\n')
		self.f.write(time.strftime('%H'+':' +'%M')+'\n')
		self.f.write('\n')
	def chk(self,r):
		try:
			open(r+'.txt','r')
		except OSError:
			print 'No entries of this date exist '
			print
			return False
		except IOError:
			print 'No entries of this date exist '
			print
			return False
		else:
			return True
	def wr(self):
		if self.chk(time.strftime('%h'+'-' +'%m'+'-'+'%y')):
			self.deco()
		print
		print 'Type your entry. When done go to a new line and type exitnow'
		while True:
			r = raw_input('')
			if r.lower() == 'exitnow':
				print 'Done'
				break
			else:
				self.f.write(r)
				self.f.write('\n')
		print 'Done'
		self.f.write('\n')
		self.f.close()

	def rea(self):
		r = raw_input('Enter the date to read its entry in the format First three letters of month-date and year. eg sep-09-16 ').capitalize()
		print 
		if self.chk(r):
			p = open(r+'.txt')
			print p.read().lstrip()
		
	def delete(self):
		import os
		r = raw_input('Enter the date whose entry you want to delete in the format First three letters of month-date and year. eg sep-09-16 ').capitalize()
		os.remove(r+'.txt')
		print 'Removed'
try:
	p = os.getcwd()
	os.mkdir(p+'/Days')
	os.chdir(p+'/Days')
except OSError:
	os.chdir(p+'/Days')
while True:
	print
	a = Diary()
	p = raw_input('''To create todays entry or add to todays entry type t. 
To view a past entry type p. 
To delete an entry type d. 
To exit type e. ''')
	if p == 't':
		a.wr()
	elif p == 'p':
		a.rea()
	elif p == 'd':
		a.delete()
	elif p == 'e':
		exit()
