import threading,time
from Core.tcp_scan import *
from Core.common import *
""""
Usage  : PortScanner.py -H ip -P port <default=0-65534>"
print "Example: PortScanner.py -H 192.168.1.1 -P 80,22,21"
print "         PortScanner.py -H 192.168.1.1-5 -P 21-100"
print "         PortScanner.py -H 192.168.1.1"
"""

def Error(msg):
    print (msg)


# 多线程调用
def tcp_scanner(ip,port):
    global dict_res,progress
    num=len(port)
    s = threading.Semaphore(500)
    lock=threading.Lock()
    start = time.clock()
    for i in ip:
        dict_res.append({i:[]})
        print ("HOST ADDRESS: %s" % i)
        print ('  PORT      STATE     SERVICE     BANNER')
        for j in port:
            #connect_scan(i,j)
            s.acquire()
            threading.Thread(target=connect_scan,args=(i,j,s,lock)).start()

    # dict_res=[{"ip":"192.168.1.1","ports":[["22","ssh v2.1","ssh"],["21","ftp v0.2","ftp"]]},{"ip":"127.0.0.1","ports":[["22","ssh v2.1","ssh"],["21","ftp v0.2","ftp"]]}]
    #dict_res=[{'192.168.1.1':[['80','http','nginx'],['443','https','nginx']]},{'192.168.1.2':[['80','http','xxx']]}]
    #print ('use:',end-start)
    # 等待结果数据保存完成
    while True:
        progress = return_progress()
        if progress==num:
            end = time.clock()
            useTime=end-start
            print("Use: "+str(useTime))
            return dict_res

# 输入处理&启动函数
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
    print (result)
    return result

