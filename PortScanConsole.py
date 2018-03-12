import sys,getopt,threading,time

from Core.common import *
from Core.tcp_scan import *


def Error(msg):
    print (msg)


def print_usage():
    helpMsg=""""
Usage  : PortScanner.py -H ip -P port <default=0-65534>"
print "Example: PortScanner.py -H 192.168.1.1 -P 80,22,21"
print "            PortScanner.py -H 192.168.1.1-5 -P 21-100"
print "            PortScanner.py -H 192.168.1.1"
    """
    print (helpMsg)



def tcp_scanner(ip,port):
    global progress
    s = threading.Semaphore(300)
    start = time.clock()
    l=threading.Lock()
    for i in ip:
        num=len(port)
        print ("HOST ADDRESS: %s" % i)
        print ('  PORT        STATE      SERVICE      BANNER')
        for j in port:
            s.acquire()
            threading.Thread(target=connect_scan,args=(i,j,s,l)).start()
        while True:
            if progress.get_progress()==num:
                break
        progress.clear_progress()
    end = time.clock()
    print("use: %f s" % (end - start))




if __name__ == '__main__':
    ipList = []
    portList = []
    close_echo = 1
    opts,args = getopt.getopt(sys.argv[1:],"hH:P:",["help","host=","port="])
    for op,value in opts:
        if op in ('-h','help'):
            print_usage()
        if op in ('-H','-host'):
            try:
                if len(value.split('.')) == 4:
                    ipList = create_list(value)
                else:
                    host = get_host_by_name(value)
                    ipList = create_list(host)
            except:
                Error("Please input the host ip address")
                print_usage()
                sys.exit()
        if op in ('-P','-port'):
            portList = create_list(value)
        else:
            portList = range(0,65534)

    tcp_scanner(ipList,portList)
