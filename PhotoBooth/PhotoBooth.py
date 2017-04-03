import SimpleCV, time,os
cam = SimpleCV.Camera()
i = 0
print 'Now before we start... Thats how you look...'
while i!= 2:
	cam.getImage().show()
	time.sleep(1)
	i += 1
	 
q = raw_input('Enter a name for the album ')
p = os.getcwd()
os.mkdir(p+'/'+q)
os.chdir(p+'/'+q)
r = int(raw_input('Enter how long you wanna take pics for in seconds '))
print 'Taking pics.. Do what you want ;P'
x = int(time.strftime('%S'))
n = 1
for a in range(r*5):
	try:
		i = cam.getImage()
		time.sleep(0.1)
		i.save(str(n)+'.jpg')
		n += 1
	except:
		pass
print 'Your photos have been saved in the album. Enjoy :)'
