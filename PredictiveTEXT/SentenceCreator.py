from Predict import predict
import random,json
while True:
	s = ''
	p = input('Enter first word: ').lower()
	s=p+' '
	for a in range(100):
		r = random.randint(1,4)
		sp = s.split()[-1]
		try:
			s+=predict(sp)[r]+' '
		except IndexError:
			try:
				r-=1
			except IndexError:
				r-=2
		#else:
		#	d = json.load(open('Data.txt'))
		#	p= d.keys()
		#	print(p)
		#	s+=predict(p[random.randint(1,len(d))])
	print(s)

