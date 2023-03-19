#import argparse
#parser=argparse.ArgumentParser
#parser.add_argument("filename")
#args=parser.parse_args
from curses.ascii import isdigit, isspace
import sys
import math
pq=list()
filename=sys.argv[1]
f = open(filename, "r")
pq=list()
message=list()
count=1
def process(pq,message):
    p=int(pq[0])
    q=int(pq[1])
    n=p*q
    phiofn=(p-1)*(q-1)
    i=0
    j=2
    coprime=list()
    while i<3:
        if math.gcd(phiofn,j)==1:
            coprime.append(j)
            j+=1
            i+=1
        else:
            j+=1
    e=coprime[2]
    d=pow(e,-1,phiofn)
    for x in range(len(message)):
     str1=message[x]
     msg=""
     for i in str1:
        msg += i
     msg=int(msg)
     c=pow(msg,e,n)
     m=pow(c,d,n)
     print("{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format("p: ",p,", q: ",q,", n: ",n,", phi: ",phiofn,", e: ",e,", d: ",d,", message: ",msg,", encrypted: ",c,", decrypted: ",m))
while True:
    line =f.readline()
    if line.find(" ")!=-1:
        pq=line.split()
    else:
        message=line.split()
        process(pq,message)

    if line.find(" ")!=-1:
        
        message.clear()
        continue
    if not line:
        break           
f.close

