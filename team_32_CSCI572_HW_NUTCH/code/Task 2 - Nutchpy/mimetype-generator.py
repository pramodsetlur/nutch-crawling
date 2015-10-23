import nutchpy
import sys

list_data=[]
mime_list=[]
node_path = "/home/sanjay/IR/nutch/runtime/local/guncrawl/crawldb/current/part-00000/data"
seq_reader = nutchpy.sequence_reader
noofrows = seq_reader.count(node_path)
list_data=(seq_reader.head(noofrows,node_path))

item='lastModified'
print(len(list_data))
for i in range(0,len(list_data),20):
    if item in list_data[i][1]:
        sublist=list_data[i][1].split()
        for k in range(0,len(sublist)):
            if 'Content-Type=image' in sublist[k] and sublist[k] not in l:
                mime_list.append(sublist[k])

for i in range(0,len(mime_list)):
    print(mime_list[i])
