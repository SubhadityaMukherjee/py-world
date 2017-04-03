class Ana:
	def __init__(self):
		self.a = str()
		self.permuted = str()
		self.final_temp = list()
		self.final = list()
		self.l = str()
	def i(self):
		r = raw_input('Enter a word ')
		self.a = r
		self.per(r)
	def per(self,en):
		from itertools import permutations
		x = ["".join(p) for p in permutations(en)]
		y = set(x)
		self.chk()
		for a in y:
			if str(a) in self.l:
				self.final_temp.append(a)
		for a in self.final_temp:
			if a not in self.final:
				self.final.append(a)	
	def chk(self):
		f = open('dictionary.txt', 'r')
		lines = f.read().split()
		self.l = lines	
	def pr(self):
		print self.final
	def save(self):
		o = open('history.txt','a')
		o.write('\n'+str(self.a)+'- '+str(self.final))
		o.close()
print 'This is a program to print anagrams of a word '
while True:
	n = raw_input('\nTo continue hit enter or type e. To view history type h. ')
	if len(n) == 0:
		p = Ana()
		p.i()
		p.pr()
		p.save()
        elif n == 'h':
                f = open('history.txt', 'r')
                x = f.read()
                print x
	else:
		break
