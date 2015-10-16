##Crawling for images of guns using Nutch
The tasks for the this assignment are present in CS572_HW_NUTCH_WEAPONS.pdf
All of the following programs use python 2.7 and java 1.8

###Task #1
For this task we have submitted our nutch-site.xml. All of the tags  in this file overrides nutch-default.xml
###Task #2
The path to the crawldb/current/part-00000/data has been hard coded in the program. To run this program against any other data this path needs to be changed inside the code

Usage: $ python mimetype-generator.py

###Task #3
We have written 2 custom handlers that Nutch will crawl
CustomLoginHandler.java - This handler finds the username and the password for each webpage dynamically. If the webpage has login abilities then we use our team email id and password to login to the website.

CustomPaginationHandler.java - This handler finds all the anchor tags and appends it to a list. Simultaneously we find the "next" button to paginate to the other pages

###Task #4
We upgraded Tika as mentioned to 1.10

###Task #5
We enabled the protocol-interactive-selenium plugin and were able to circumvent many URLs that were not crawled initally

###Task #6
Execute 
$ bin/nutch mergesegs <output_dir1> -dir <path_to_segment_dir> 
$ bin/nutch readseg -dump <<PATH_TO_SEGMENTS_OF_output_dir1> <OutputDIR_2> -nocontent -nofetch -nogenerate -noparse -noparsedata

The dump file genereated from above is used by image_metadata.py

$ python image_metadata.py
This will create 2 files - URLlist.txt and image_metadata.txt
URLlist.txt - List of image URLs
image_metadata.txt - Metadata of the image urls

You will need the above files to execute either exactduplicates.py or nearduplicates.py
Both of the above file names have been hard coded in the files below.

a.
$ python exactduplicates.py

b.
$ python nearduplicates.py

###Task #7
We followed the instuctions at Nutch similarity scoring filter's GitHub link.

###Task #8
This task is to crawl inside Nutch server
$ python nutch_server_crawl.py weapons-seeds.txt

###Task #9 
This tak is to run the tika-similarity over the crawled data
python similarity.py -f crawl_images
python value-similarity.py -f crawl_images
python cluster-scores.py 
open cluster-d3.html

###Task #10
This task is to run the crawls using Memex-explorer
Execute the following command in memex environment in Anaconda.
crawl ~/urls /tmp/output 3


