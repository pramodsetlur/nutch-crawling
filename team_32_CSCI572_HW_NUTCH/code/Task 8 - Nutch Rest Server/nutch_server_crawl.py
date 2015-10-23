from nutch.nutch import Nutch
from nutch.nutch import SeedClient
from nutch.nutch import Server
from nutch.nutch import JobClient
import nutch
import sys

sv=Server('http://localhost:8081')
sc=SeedClient(sv)

# reading the seed file from the command line
inputdata=open(sys.argv[1],'r')
# reading the seed file line by line
for line in inputdata:
    seed_urls=(line)
    sd= sc.create('seed',seed_urls) 

    nt = Nutch('default')
    jc = JobClient(sv, 'test', 'default')
    cc = nt.Crawl(sd, sc, jc)   
    while True:
        job = cc.progress() # gets the current job if no progress, else iterates and makes progress
        if job == None:
            print "no more jobs"
            break 
