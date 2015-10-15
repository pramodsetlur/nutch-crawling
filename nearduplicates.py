import md5
URLlist = []
meta_list = []
neardup_dict = {}

def convert_hextobin(m1):
	str=""
	for i in range(0,len(m1)):
		if m1[i] == '0':
			str+='0000'
		elif m1[i] == '1':
			str+='0001'
		elif m1[i] == '2':
			str+='0010'
		elif m1[i] == '3':
			str+='0011'
		elif m1[i] == '4':
			str+='0100'
		elif m1[i] == '5':
			str+='0101'
		elif m1[i] == '6':
			str+='0110'
		elif m1[i] == '7':
			str+='0111'
		elif m1[i] == '8':
			str+='1000'
		elif m1[i] == '9':
			str+='1001'
		elif m1[i] == 'a':
			str+='1010'
		elif m1[i] == 'b':
			str+='1011'
		elif m1[i] == 'c':
			str+='1100'
		elif m1[i] == 'd':
			str+='1101'
		elif m1[i] == 'e':
			str+='1110'
		elif m1[i] == 'f':
			str+='1111'
	return str

def read_inputfile():
	global URLlist, meta_list
	fr = open('URLlist.txt','r')
	lines = fr.readlines()
	for line in lines:
		URLlist.append(line.strip('\n'))
	fr.close()
	
	fr = open('parsetext','r')
	lines = fr.readlines()
	for line in lines:
		meta_list.append(line.strip('\n'))
	fr.close()
	
def init_simhash():
	simhash=[]
	for i in range(0,128):
		simhash.append(0)
	return simhash

	
def calculate_shingles(string1, shingle_size):
	shingle_list=[]
	for i in range(0,len(string1)-shingle_size+1):
		str=""
		j = i
		for k in xrange(shingle_size):
			str+=string1[j]
			j += 1
		shingle_list.append(str)
	return shingle_list

def global_fingerprintutil(hashval,V):
	for i in range(0,len(hashval)):
		if hashval[i] == '0':
			V[i]+=1
		else:
			V[i]-=1
	return V
	
def get_global_fingerprint(shingle_list,V):
	for i in range(0,len(shingle_list)):
		hash_val=md5.new(shingle_list[i]).hexdigest()
		hash_val=convert_hextobin(hash_val)
		#print hash_val
		V = global_fingerprintutil(hash_val,V)
	calculate_simhash(V)
	return V

def calculate_simhash(V):
	for i in range(0,len(V)):
		if V[i] >= 0:
			V[i]=1
		else:
			V[i]=0
	return V
	
def getsimhash(string):
	simhash=init_simhash()
	shingle_size = 4
	shingle_list=calculate_shingles(string, shingle_size)
	simhash=get_global_fingerprint(shingle_list,simhash)
	return simhash


def calculate_similarity(simhash1,simhash2):
	similarity_count=0
	for i in range(0,len(simhash1)):
		if simhash1[i] == simhash2[i]:
			similarity_count+=1
	similarity_percentage = (similarity_count*100)/len(simhash1)
	return similarity_percentage

def start():
	global URLlist,meta_list,neardup_dict
	read_inputfile()
	for i in range(0,len(URLlist)-1):
		for j in range(i+1,len(URLlist)):
			simhash1 = getsimhash(meta_list[i])
			simhash2 = getsimhash(meta_list[j])
			similarity_percent=calculate_similarity(simhash1,simhash2)
			
			if similarity_percent >= 90:
				if URLlist[i] not in neardup_dict.keys():
					val_list=[]
					val_list.append(URLlist[j])
					neardup_dict[URLlist[i]] = val_list
				else:
					neardup_dict[URLlist[i]].append(URLlist[j])
					
				if URLlist[j] not in neardup_dict.keys():
					val_list=[]
					val_list.append(URLlist[i])
					neardup_dict[URLlist[j]] = val_list
				else:
					neardup_dict[URLlist[j]].append(URLlist[i])

	if not neardup_dict:
		print "No near duplicates found"
	else:
		print "Based on the metadata of images, the near duplicate image URLs identified are as follows:"
		i=0
		for key,val in neardup_dict.iteritems():
			i+=1
			print "URL"+str(i)+"::",key
			print "Near duplicates are:"
			for item in val:
				print item
			print "\n"
	


start()
			
