import tika
tika.initVM()
from tika import parser
URLlist = []

# Reads dump file and extracts only image URLs and writes to a file called URLlist.txt
def read_dump():
	fr = open('dump','r')
	fw = open('URLlist.txt','w')
	lines = fr.readlines()
	for i in range(0,len(lines)):
		sublist = []
		if lines[i].startswith("URL"):
			sublist = lines[i].split(":: ")
			if len(sublist) > 1:
				if sublist[1].endswith("jpg\n") or sublist[1].endswith("JPG\n") or sublist[1].endswith("png\n") or sublist[1].endswith("PNG\n") or sublist[1].endswith("gif\n") or sublist[1].endswith("GIF\n") or sublist[1].endswith("bmp\n") or sublist[1].endswith("BMP\n"):
					fw.write((sublist[1].strip('\n'))+'\n')
					
	fr.close()
	fw.close()

# Reads URLlist.txt and extracts metadata from the image URLs using tika parser and writes the metadata to image_metadata.txt	
def extract_metadata():
	global URLlist
	
	fr = open('URLlist.txt','r')
	lines = fr.readlines()
	for line in lines:
		URLlist.append(line.strip('\n'))
	fr.close()
	
	fw = open('image_metadata.txt','w')
	for i in range(0,len(URLlist)):
		parsed = parser.from_file(URLlist[i])
		for k,v in parsed["metadata"].iteritems():
			if k != 'File Name':
				fw.write(k)
				try:
					fw.write(str(v))
				except UnicodeEncodeError:
					fw.write(str(v.encode('utf-8')))
		fw.write('\n')
	fw.close()

def main():
	read_dump()
	extract_metadata()

if __name__ == '__main__':
	main()