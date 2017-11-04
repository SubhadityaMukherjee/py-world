import json, collections
f = open('Data.txt','a+',encoding = 'utf-8',errors = 'ignore')
o = open('dat.txt','r',encoding = 'utf-8',errors = 'ignore')
h = open('history.txt','a+',encoding = 'utf-8',errors = 'ignore')
ntsp = list(r"\<>?/!@#$%^&*()_-+=,.")
nt = [r"\"",r"\'"]+ntsp
datin = o.read().encode('ascii','ignore').decode('utf-8')
dat = datin.split()
datli = []

d = json.load(open('Data.txt'))
def createword():
	for x in dat:
		a = x.lower().rstrip()
		if (a[-1] in nt) or (a[-1].isdigit()):
			a = a[0:-1]
		datli.append(a)
		if a not in nt or a.isdigit()!= True:
			if a not in d:
				d[a] = []


def add():
	for p in datli:
		a = p
		for b in range(len(datli)-1):
			if( a == datli[b]):
				if a not in d.keys():			#edited
					d[a].append(dat[b+1])		#edited

def rank():
	for a in d.keys():
		p = d[a]
		p.sort()
		rank = collections.Counter(d[a]).most_common(4)
		l =[]
		for b in rank:
			l.append(b[0])
		d[a] = l
	f = open('Data.txt','w+')
	f.write(json.dumps(d))

def predict(i):
	try:
		if i in d.keys():
			return(d[i])
		else:
			return(['More predictions coming soon'])
	except:
		print('Please input properly')

def fortheword():
	createword()
	add()
	f.write(json.dumps(d))
	rank()

def writetext():
	try:
		s = ''
		print('Enter text word by word. If you dont want predictions, just type and hit enter. To choose a word from prediction,type its no in the list (1 or 2 or 3 or 4). To end typing type exitnow and hit enter')
		while True:
			i = input().rstrip().lower()
			if i == 'exitnow':
				h.write(s+'\n')
				break
			punctuation = list(".,?!")
			if i in punctuation:
				s+=i+' '
				continue
			l = predict(i)
			if l == ['More predictions coming soon']:
				s+=i+' '
				continue
			print(l)
			n = input()
			if len(n) == 0:
				s+=' '+i
				print(s)
			else:
				s+=' '+i
				s+= ' '+l[int(n)-1]
				print(s)
		print(s)
	except:
		pass

#fortheword()
#writetext()
