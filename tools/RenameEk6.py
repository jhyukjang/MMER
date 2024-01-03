from glob import glob
import os
import pdb


filelist=glob("/mnt/server18_hard0/jhjang/AVER/VAANet/data/ek6/ek6--imgs/*/*")

cnt=1

filelist.sort()

print(filelist)

class_dict={
    'anger':1,
    'disgust':2,
    'fear':3,
    'joy':4,
    'sadness':5,
    'surprise':6
}


"""
with open("annotations/ek6/trainlist01.txt",'w') as f:
    for file in filelist:
        name=file.split('/')[-2]+"/"+file.split('/')[-1]
        # pdb.set_trace()
        if cnt%2==1:
            f.write(name+" "+str(class_dict[file.split('/')[-2]])+"\n")
        cnt+=1 
"""


with open("annotations/ek6/testlist01.txt",'w') as f:
    for file in filelist:
        name=file.split('/')[-2]+"/"+file.split('/')[-1]
        # pdb.set_trace()
        if cnt%2==0:
            f.write(name+" "+str(class_dict[file.split('/')[-2]])+"\n")
        cnt+=1 