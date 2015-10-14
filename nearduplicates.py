import md5
import tika
tika.initVM()
from tika import parser

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


def init_simhash():
	simhash=[]
	for i in range(0,128):
		simhash.append(0)
	return simhash

	
def calculate_shingles(string1):
	shingle_list=[]
	
	for i in range(0,len(string1)-1):
		str=""
		str+=string1[i]
		str+=string1[i+1]
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
		print hash_val
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
	shingle_list=calculate_shingles(string)
	print shingle_list
	simhash=get_global_fingerprint(shingle_list,simhash)
	return simhash


def calculate_similarity(simhash1,simhash2):
	similarity_count=0
	for i in range(0,len(simhash1)):
		if simhash1[i] == simhash2[i]:
			print "inside cal sim"
			similarity_count+=1
	print "similarity count", similarity_count
	similarity_percentage = (similarity_count*100)/len(simhash1)
	return similarity_percentage

def start():
	simhash1=getsimhash("Shakespeare produced most of his known work between 1589 and 1613")
	simhash2=getsimhash("Shakespeare produced most of his work after 1589")
	similarity_percent=calculate_similarity(simhash1,simhash2)
	print similarity_percent
	print simhash1
	print simhash2
	
	

start()
			