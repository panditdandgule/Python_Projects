import re
import sys

#Accesslog file path
file="E:\\PYTHON\\Python_Aim\\PYTHON\\PY_Projects\\Projects\\access_log"

#Append ip address
x=[]
occurence={}
#open a file
with open(file) as f:
    #Read all lines already in the file
    for line in f:
        ip=re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',line)
        for i in ip:
            x.append(i)
    for ipaddr in x:
        if ipaddr in occurence:
            occurence[ipaddr]=occurence[ipaddr]+1
        else:
            occurence[ipaddr]=1

    for key,value in occurence.iteritems():
        print(key,value)

print(f.read())

