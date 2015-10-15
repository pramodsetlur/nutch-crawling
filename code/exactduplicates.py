import md5


URLlist = []
URLdict = {}
Dup_URL_list = []	

# Reads URLlist.txt and stores the image URLs in a list
def read_URLlist():	
	global URLlist
	fr = open('URLlist.txt','r')
	lines = fr.readlines()
	for i in range(0,len(lines)):
		URLlist.append(lines[i])
	fr.close()

# Finds exact duplicate image URLs by using md5 python lib to calculate hash values 
def find_duplicateURLs():
	global URLdict, Dup_URL_list, URLlist
	fr = open('image_metadata.txt','r')
	lines = fr.readlines()
	
	for i in range(0,len(lines)):
		met = ""
		for j in range(0,len(lines[i]),5):
			met+=lines[i][j]
		hashval = md5.new(met).hexdigest()
		if str(hashval) in URLdict.values():
			Dup_URL_list.append(URLlist[i])
			for url,val in URLdict.iteritems():
				if val == hashval and url not in Dup_URL_list:
					Dup_URL_list.append(url)
		else:
			URLdict[str(URLlist[i])] = str(hashval)
	
	fr.close()

	if len(Dup_URL_list) > 0:
		print "The exact duplicate image URLs are:"
		for i in range(0,len(Dup_URL_list)):
			print Dup_URL_list[i]
	else:
		print "No exact Duplicate image URLs"

def main():
	read_URLlist()
	find_duplicateURLs()
	

if __name__ == '__main__':
	main()
