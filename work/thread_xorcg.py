# coding:utf-8
# author:csp
# updata time 2018-2-1
#develop this code by python 2.7

import socket
import time
import threading

class Client:
    def __init__(self, ip, port, layer, flash):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s = s
        self.Port = port
        self.IP = ip
        self.layer = layer
        self.flash = flash

#if s.sendall fail,try to connect
    def sendall(self, cmd):
        try:
            self.s.sendall(cmd)
            return True
        except socket.error, e:
            print "send data fail,error happen %s" % e
            self.Connect()
            print "tcp reconnect ok"



# load all layer flash
    def send_load(self):
        for layer in range(self.layer):
            Load = "R0"+bytes(layer)+self.flash[layer]+":"
            self.sendall(Load)
            print "load flash%s" % Load

# cutup all layer flash
    def send_cutup(self):
        for layer in range(self.layer):
            Cut_up = "3"+bytes(layer)+" 1:"
            self.sendall(Cut_up)


# cutdown all layer flash
    def send_cutdown(self):
        for layer in range(self.layer):
            Cut_down = "3" + bytes(layer) + " 0:"
            self.sendall(Cut_down)

# erase all layer flash
    def send_Erase(self):
        for layer in range(self.layer):
            Erase = "A" + bytes(layer) + ":"
            self.sendall(Erase)

# restart all layer flash

    def restart(self):
        for layer in range(self.layer):
            Restart = "s4" + bytes(layer) + ":"
            self.sendall(Restart)

# pause all layer flash
    def pause(self):
        for layer in range(self.layer):
            Pause = "s1" + bytes(layer) + "0:"
            self.sendall(Pause)

    def Connect(self):
        print "try to connect port %d\n" % self.Port
        while True:
            if self.Con_Tcp() is True:
                print " %d connect ok " % self.Port
                break
            print " %d connect fail " % self.Port
            time.sleep(1)

# try to connect every decoder by TCPIP

    def Con_Tcp(self):
        try:
            self.s.connect((self.IP, self.Port))
            return True
        except socket.error, e:
            print e
            return False

# close the connection of TCPIP
    def discon_TCP(self):
        self.s.close()
# if network has something wrong


    def Case1(self):
        case1_times = 0
        self.Connect()
        while case1_times < 1000:
            try:
                self.send_load()
                self.send_cutup()
                time.sleep(5)
                self.send_cutdown()
                case1_times = case1_times+1
                print "case1 has test %d times\n" % case1_times
                continue
            except socket.error, e:
                print "send data fail some error happen %s\n" % e

        print "case1 is test over\n"


    def Case2(self):
        if self.Con_Tcp() is True:
            self.send_load()
            time.sleep(1)
            self.send_cutup()
            time.sleep(5)
            self.send_cutdown()

        else:
            print "%d instance connect fail\n" % self.Port




#####多线程并发发送数据
    def MyThreading(self, case):
        MyThread = threading.Thread(target=case)
        print "%d instance enter thread" % self.Port
        MyThread.start()
        print "%d instance leave thread" % self.Port




if __name__ == "__main__":
    for p in [3001, 3003, 3005, 3007]:
        con = Client(ip="10.20.0.129", port=p, layer=8,  flash=["zmz.swf", "cc.swf", "1080i50-ei.swf", "CCTV_BD.swf", "1080i50-LOGO-FengYunZuQiu-L.swf", "CCTV_BD.swf",
                 "1080i-clock.swf", "dve.swf"])
        con.MyThreading(con.Case1)
