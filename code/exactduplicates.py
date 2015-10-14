import md5
import tika
tika.initVM()
from tika import parser

URLlist = []
URLdict = {}
Dup_URL_list = {}
def read_dump():
	global URLlist
	fr = open('dump','r');
	lines = fr.readlines()
	for i in range(0,len(lines)):
		sublist = []
		if lines[i].startswith("URL"):
			sublist = lines[i].split(":: ")
			if len(sublist) > 1:
				if sublist[1].endswith("jpg\n") or sublist[1].endswith("JPG\n") or sublist[1].endswith("png\n") or sublist[1].endswith("PNG\n") or sublist[1].endswith("gif\n") or sublist[1].endswith("GIF\n") or sublist[1].endswith("bmp\n") or sublist[1].endswith("BMP\n"):
					URLlist.append(sublist[1].strip('\n'))
			#URLlist.append(sublist[0])
	fr.close()
	
	fw = open('URLlist.txt','w')
	for i in range(0,len(URLlist)):
		fw.write(URLlist[i]+'\n')
	fw.close()

def extract_metadata():
	fw = open('parsetext','w')
	for i in range(0,20):
		parsed = parser.from_file(URLlist[i])
		for k,v in parsed["metadata"].iteritems():
			fw.write(k)	
			try:
				fw.write(str(v))
			except UnicodeEncodeError:	
				fw.write(str(v.encode('utf-8')))
		fw.write('\n')
	fw.close()

def find_duplicateURLs():
	global URLdict, Dup_URL_list, URLlist
	fr = open('parsetext','r')
	lines = fr.readlines()
	met = ""
	for i in range(0,len(lines)):
		for j in range(0,len(lines[i]),5):
			met+=lines[i][j]
		hashval = md5.new(met).hexdigest()
		if hashval not in URLdict.values():
			URLdict[URLlist[i]]	= hashval
		else:
			for url,val in URLdict:
				if val == hashval:
					Dup_URL_list.append(url)
					Dup_URL_list.append(URLlist[i])
	
	if len(Dup_URL_list) > 0:
		for i in range(0,len(Dup_URL_list)):
			print Dup_URL_list[i]
	else:
		print "No exact duplicate URLs"
			  
def start():
	read_dump()
	extract_metadata()
	find_duplicateURLs()
	

start()
