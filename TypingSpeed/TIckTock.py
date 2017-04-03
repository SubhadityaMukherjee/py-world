#author: Subhaditya Mukherjee
import time
m = int(time.strftime('%M'))
s = int(time.strftime('%S'))
ti = m*60 + s
r = raw_input('Type ')
mm = int(time.strftime('%M'))
ss = int(time.strftime('%S'))
tf = mm*60 + ss
Time = tf-ti

def Len(r):
	c = 0
	for a in r:
		c += 1
	return c
print Len(r)
print Time
print 'Speed = ', Len(r)/Time , ' char/sec (- a few characters)'
