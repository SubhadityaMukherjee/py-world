import os
import argparse
from bs4 import BeautifulSoup
import urllib.request

ap = argparse.ArgumentParser()
ap.add_argument("-m", "--music", required=True,
				help="path to input music")
args = vars(ap.parse_args())
os.chdir(args['music'])

def getLinks(name):
	link = b'https://search.azlyrics.com/search.php?q={}'.decode('ASCII').format(name)
	#print(link)
	site = urllib.request.urlopen(link)
	soup = BeautifulSoup(site, 'html.parser')
	list_of_links = []
	for link in soup.find_all('a'):
		#print('no{}'.format(link))
		if('/lyrics/' in link.get('href')):
			list_of_links.append(link.get('href'))
			#'finallygot{}'.format(link.get('href'))
	try:
		return list_of_links[0]
	except IndexError:
		return 'https://google.com'


def formatLyrics(f_name):
	fp = open(f_name,'r')
	f = fp.readlines()
	#print(f[5])
	#print(f_name.replace('w.txt','.txt'))
	f1 =open(f_name.replace('w.txt','.txt'),'a+')
	s = 0
	for a in f:
		s+=1
		if 'Android' in a:
			break
	#print('\n'.join(f[147:s-1]))
	f1.write('\n'.join(f[147:s-1]))
	f1.close()
	os.remove(f_name)



def getLyrics(name):
	#print('Getting lyrics')
	#print(name)
	p = getLinks(name)
	site = urllib.request.urlopen(p)
	soup = BeautifulSoup(site, 'html.parser')
	#print(soup.text)
	#ly = soup.find("div",{"class":})
	f_name = '{}w.txt'.format(name.replace('+',' '))
	f = open(f_name,'a+')
	#print(soup.text)
	f.write(soup.text)
	f.flush()
	f.close()
	formatLyrics(f_name)


def formatinput(string):
	ps = string
	if '(' in ps:
		b1,b2 = ps.find('('),ps.find(')')
		ps = ps[0:b1+1]+ps[-b2:-1]
	if '[' in ps:
		b1,b2 = ps.find('['),ps.find(']')
		ps = ps[0:b1+1]+ps[-b2:-1]
	if 'ft' in ps:
		ind = ps.find('ft')
		ps = ps[0:ind+1]+ps[-3:-1]
	if ps[0].isdigit():
		ps = ps[2::]
	if '-' in ps:
		ps = ps.replace('-',' ')
	if '_' in ps:
		ps = ps.replace('_',' ')
	if '.' in ps:
		ps = ps.replace('.',' ')
	if '%' in ps:
		ps = ps.replace('%',' ')
	return ps

def for_all_files():
	for root,dirs,files in os.walk(".", topdown=False):
		for name in files:
			if 'DS' not in name:
				#print(name)
				name = formatinput(name)
				print(name)
				namstring = name[:-4].split()
				new_name = '+'.join(namstring)
				#print(new_name)
				try:
					getLyrics(new_name)
				except:
					if '-' in new_name:
						ps = new_name
						ind = ps.find('-')
						ps = ps[0:ind-1]+ps[ind:ind+1]+ps[-3:-1]
						getLyrics(ps)
				else:
					print('Lyrics not found for this one.')
for_all_files()



