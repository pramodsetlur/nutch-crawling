''' Simhash Algorithm implementation
    Reference: http://www.titouangalopin.com/blog/2014-05-29-simhash
               http://matpalm.com/resemblance/simhash/


    USAGE: This python program needs a two files - URL list file containing list of image urls and
           image_metadata.txt -- which contains the metadata obtained from tika python
'''
import md5
URLlist = []
meta_list = []
''' near duplicate dictionary.
    This contains a url as the key of the dictionary and value as all the duplicated urls

    This dictionary will be determined based on the metadata generated for the given image
'''
neardup_dict = {}

''' This API converts hexadecimal 32 bit md5 hash to 128 bit binary'''
def convert_hextobin(hex_val):
	binary=""
	for i in range(0,len(hex_val)):
		if hex_val[i] == '0':
			binary += '0000'
		elif hex_val[i] == '1':
			binary += '0001'
		elif hex_val[i] == '2':
			binary += '0010'
		elif hex_val[i] == '3':
			binary += '0011'
		elif hex_val[i] == '4':
			binary += '0100'
		elif hex_val[i] == '5':
			binary += '0101'
		elif hex_val[i] == '6':
			binary += '0110'
		elif hex_val[i] == '7':
			binary += '0111'
		elif hex_val[i] == '8':
			binary += '1000'
		elif hex_val[i] == '9':
			binary += '1001'
		elif hex_val[i] == 'a':
			binary += '1010'
		elif hex_val[i] == 'b':
			binary += '1011'
		elif hex_val[i] == 'c':
			binary += '1100'
		elif hex_val[i] == 'd':
			binary += '1101'
		elif hex_val[i] == 'e':
			binary += '1110'
		elif hex_val[i] == 'f':
			binary += '1111'
	return binary

''' 
    Accepts two files
    1. URL file containing list of all image urls
    2. Metadata file containing image for all the urls in the URL file
'''
def read_inputfile():
	global URLlist, meta_list
	fr = open('URLlist.txt','r')
	lines = fr.readlines()
	for line in lines:
		URLlist.append(line.strip('\n'))
	fr.close()
	
	fr = open('image_metadata.txt','r')
	lines = fr.readlines()
	for line in lines:
		meta_list.append(line.strip('\n'))
	fr.close()
	
def init_simhash():
	simhash=[]
	for i in range(0,128):
		simhash.append(0)
	return simhash

''' 
    Determines all shingles of specified shingle size for a given string in a list
'''	
def calculate_shingles(string1, shingle_size):
	shingle_list=[]
	for i in range(0,len(string1)-shingle_size+1):
		str=""
		j = i
		for count in xrange(shingle_size):
			str+=string1[j]
			j += 1
		shingle_list.append(str)
	return shingle_list

def global_fingerprint_util(hashval, global_fingerprint):
	for i in range(0,len(hashval)):
		if hashval[i] == '0':
			global_fingerprint[i]+=1
		else:
			global_fingerprint[i]-=1
	return global_fingerprint
	
def get_global_fingerprint(shingle_list, global_fingerprint):
	for i in range(0,len(shingle_list)):
		hash_val=md5.new(shingle_list[i]).hexdigest()
		hash_val=convert_hextobin(hash_val)
		#print hash_val
		global_fingerprint = global_fingerprint_util(hash_val, global_fingerprint)
	calculate_simhash(global_fingerprint)
	return global_fingerprint

def calculate_simhash(global_fingerprint):
	for i in range(0,len(global_fingerprint)):
		if global_fingerprint[i] >= 0:
			global_fingerprint[i]=1
		else:
			global_fingerprint[i]=0
        return global_fingerprint  
	
def getsimhash(string):
	simhash=init_simhash()
        #fix the shingle size as 4, this can be experimented but 4 is recommended for near duplicates
	shingle_size = 4
	shingle_list=calculate_shingles(string, shingle_size)
	simhash=get_global_fingerprint(shingle_list,simhash)
	return simhash

''' 
    Given two simhashes, It determines the similarity by comparing the number of bits that 
    two hashes are in common with
'''
def calculate_similarity(simhash1, simhash2):
	similarity_count = 0
	for i in range(0,len(simhash1)):
		if simhash1[i] == simhash2[i]:
			similarity_count+=1
	similarity_percentage = (similarity_count*100)/len(simhash1)
	return similarity_percentage

def main():
	global URLlist,meta_list,neardup_dict
	read_inputfile()
	for i in range(0,len(URLlist)-1):
        ''' Un comment the below line and comment the above line to test the program for partial data'''
	#for i in range(0,4):
		#for j in range(i+1,4):
        ''' Un comment the below line and comment the above line to test the program for partial data'''
		for j in range(i+1,len(URLlist)):
			simhash1 = getsimhash(meta_list[i])
			simhash2 = getsimhash(meta_list[j])
			similarity_percent=calculate_similarity(simhash1,simhash2)
                        
                        print similarity_percent
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
	
if __name__ == '__main__':
    main()
