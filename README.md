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
We upgraded Tika as mentioned to 1.1-SNAPSHOT

###Task #5
We enabled the protocol-interactive-selenium plugin and were able to circumvent many URLs that were not crawled initally

###Task #6
Execute 
$ python image_metadata.py
This will create 2 files - URLlist.txt and image_metadata.txt
URLlist.txt - List of image URLs
image_metadata.txt - Metadata of the image urls

a. You will need the above files to execute either exactduplicates.py or nearduplicates.py
Both of the above file names have been hard coded in the files below.

$ python exactduplicates.py

b. python nearduplicates.py

###Task #7
