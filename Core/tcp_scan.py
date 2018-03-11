# -*- coding: utf-8 -*-
import socket
# 进度判断
progress=0
#储存扫描结果
dict_res = []

def return_progress():
    return progress

# TCP全连接扫描
def connect_scan(targetHost,targetPort,t,lock):
    global progress
#def connect_scan(targetHost,targetPort):
    targetPort = int(targetPort)
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(0.5)
        res = s.connect_ex((targetHost,targetPort))
        if res == 0:
            s.send(b'PortScan')
            banner = s.recv(1024)  # 获取Banner
            service = socket.getservbyport(targetPort)  # 获取服务名
            #lock.acquire()
            print ('[+] ' + str(targetPort) + " " * (6 - (len(str(targetPort)) - 2)) + 'open       ' + service + " " * (
            9 - (len(str(service)) - 2)) + str(banner).replace('\r\n','').strip())
            s.close()
            result=[str(targetPort),str(service),str(banner)]
            result_append(targetHost,result)
            progress += 1
            #lock.release()
            #print (progress)
            #return [str(targetPort),str(service),str(banner)]
        else:
            progress += 1
    except Exception as e:
        pass
        #lock.acquire()
        #print ('[-] ' + str(targetPort) + " " * (6 - (len(str(targetPort)) - 2)) + str(e))
        #lock.release()
    t.release()


def result_append(ip,result):
    global dict_res
    for i in dict_res:
        if list(i.keys())[0]==ip:
            flag=dict_res.index(i)
            dict_res[flag][ip].append(result)