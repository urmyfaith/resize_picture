# -*- coding: utf-8 -*-

import Image
import os
import os.path
import sys
import time

fp=open('log.info','a+')
path=os.path.dirname(__file__)
#print path
time_now=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

i=1
for  root, dirs,files in os.walk(path):
    #print "files=",files
    current_dir=root
    #handel files:
    if not len(files):
        pass
    else:
        k=1
        for f in files:
            if f.endswith('.jpg') :
                #print "current_dir=",current_dir
                #print f," --> is jpg file"
                filepath = os.path.join(current_dir,f)
                #print filepath
                total_number = "%03d" % i
                file_in_dir_number = "%03d" % k
                i = i+1
                k = k+1
                try:   
                    img = Image.open(filepath)
                    w,h = img.size
                    img.resize((w/2,h/2)).save(filepath,"JPEG")
                    log_info=str(total_number)+"\t"+"SMALLSIZE\t"+current_dir+"\t"+ \
                              file_in_dir_number+"\t"+f+"\t"+str(w)+"\t"+str(h)+ \
                              "\tSUCESS\t"+str(w/2)+"\t"+str(h/2)+"\t"+time_now
                except:
                    log_info=str(total_number)+"\t"+"SMALLSIZE\t"+current_dir \
                              +"\t"+file_in_dir_number+"\t"+f+"\t"+"width"+"\t"+"height" \
                              +"\tSUCESS\t"+"width_s"+"\t"+"height_s"+"\t"+time_now
                print log_info
                fp.write(log_info+"\n")
fp.close()
