#encoding:utf-8
#Socket client example in python
import socket #for sockets
import os
import random,time
import datetime
import time
#delete all log
#define global max and min wait load sleeptime (t1,t2)
print"play video and up swf\n".decode('utf-8').encode('gbk')
#COPY rpctest.exe
instances = 4
hostname = socket.gethostname()
remote_ip = socket.gethostbyname(hostname)
videoname = "PAL_HD_1080i"
video_duration = "60"

os.system ("xcopy /s /y %s %s" % ("C:\\SeaChange\\eXd\\tools\\RpcTest.exe", "C:\\SeaChange\\eXd\\exe\\RpcTest.exe"))
def playvideo():
    for i in range(1,instances+1):
        i = bytes(i)
        f = open("C:\\SeaChange\\eXd\\exe\\decoder"+i+".scd","w")
        f.write("Set node "+hostname+"\n")
        f.write("sleep 10\n")
        f.write("Decoder connect MC_HD_DECODER"+i+"\n")
        f.write("sleep 10\n")
        def playvideo():
            f.write("Decoder cue "+videoname+"\n")
            f.write("sleep 10\n")
            f.write("Decoder play\n")
            #f.write("sleep 1\n")##4k if have'nt this ,exd will be crash 
            f.write("Decoder cue "+videoname+"\n")
            f.write("sleep "+video_duration+"\n")
            f.write("Decoder play\n")
            #f.write("sleep 1\n")
        looptimes = 1
        while looptimes < 100000:
            looptimes = looptimes + 1
            playvideo()    
        f.close
        os.startfile("C:\\SeaChange\\eXd\\exe\\decoder"+i+".scd")
        print "decoder"+i+" play video"
playvideo()
#Connect to remote server
 
     
        

    
 
