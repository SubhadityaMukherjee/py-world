import random
l = list()
p = {1:'H',2:'T'}
z = ['__','_ _', '__ ; _ _', '_ _, __']
def threecoin():
	s = ''
	for a in range(3):
		x= random.randint(1,2)
		s += p[x]
	h = s.count('H')
	t = s.count('T')
	
	if h == 0 and t == 3:
		return z[3]
	elif h == 1 and t == 2:
		return z[0]
	elif h == 2 and t == 1:
		return z[1]
	elif h == 3 and t == 0:
		return z[2]

for no in range(6):
	r = raw_input('Hit anything to toss three coins')
	if len(r) == 0 or len(r)!= 0:
		x = threecoin()
		print x
		l.append(x)
		
l.reverse()
print 
print
for a in l:
	print a
