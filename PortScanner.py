import threading,time
from Core.tcp_scan import *
from Core.common import *
""""
Usage  : PortScanner.py -H ip -P port <default=0-65534>"
print "Example: PortScanner.py -H 192.168.1.1 -P 80,22,21"
print "            PortScanner.py -H 192.168.1.1-5 -P 21-100"
print "            PortScanner.py -H 192.168.1.1"
"""

def Error(msg):
    print (msg)



def tcp_scanner(ip,port):
    global progress
    progress.clear_progress()
    num=len(port)*len(ip)
    s = threading.Semaphore(500)
    lock=threading.Lock()

    for i in ip:
        progress.dict_append({i:[]})
        print ("HOST ADDRESS: %s" % i)
        print ('  PORT        STATE      SERVICE      BANNER')
        for j in port:
            s.acquire()
            threading.Thread(target=connect_scan,args=(i,j,s,lock)).start()
    while True:
        if progress.get_progress()==num:
            print("done")
            return progress.get_result()


def start(host,ports=range(0,10000)):
    if len(host.split('.')) == 4:
        ipList = create_list(host)
    else:
        value = get_host_by_name(host)
        ipList = create_list(value)
    if type(ports)==str:
        portList = create_list(ports)
    else:
        portList=ports
    result=tcp_scanner(ipList,portList)
    #print (result)
    return result