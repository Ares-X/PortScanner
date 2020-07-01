# -*- coding: utf-8 -*-
import socket

class Progress:
    progress=0
    dict_res=[]
    def get_progress():
        return Progress.progress
    def add_progress():
        Progress.progress+=1
    def clear_progress():
        Progress.progress=0
        Progress.dict_res=[]
    def dict_append(str):
        Progress.dict_res.append(str)
    def result_append(ip,result):
        for i in Progress.dict_res:
            if list(i.keys())[0]==ip:
                flag=Progress.dict_res.index(i)
                Progress.dict_res[flag][ip].append(result)
    def get_result():
        return Progress.dict_res

progress=Progress


def connect_scan(targetHost,targetPort,t,lock):
    global progress
    targetPort = int(targetPort)
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(3)
        res = s.connect_ex((targetHost,targetPort))
        if res == 0:
            s.send(b'PortScan')
            try:
                banner = s.recv(2048)
            except:
                banner = ""

            s.close()
            service = socket.getservbyport(targetPort)
            #lock.acquire()
            print ('[+] ' + str(targetPort) + " " * (6 - (len(str(targetPort)) - 2)) + 'open       ' + service + " " * (
            9 - (len(str(service)) - 2)) + str(banner).replace('\r\n','').strip())
            
            
            result=[str(targetPort),str(service),str(banner)]
            progress.result_append(targetHost,result)
            progress.add_progress()
            #lock.release()
            #print (progress)
            return [str(targetPort),str(service),str(banner)]
        else:
            progress.add_progress()
    except Exception as e:
        progress.add_progress()
        #lock.acquire()
        print ('[-] ' + str(targetPort) + " " * (6 - (len(str(targetPort)) - 2)) + str(e))
        #lock.release()
    t.release()
