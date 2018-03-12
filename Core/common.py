# -*- coding: utf-8 -*-

from urllib.parse import urlparse
import socket

def create_list(x):
    List = []
    x = str(x)
    if ',' in x:
        List = x.split(',')
        return List
    list = x.split('.')
    if '-' in x:
        for i in list:
            d = i
            if '-' in d:
                p = list.index(d)
                l = d.split('-')
                m = int(l[0])
                n = int(l[1])
        for j in range(m,n + 1):
            list[p] = str(j)
            ip = '.'.join(list)
            List.append(ip)
    else:
        ip = '.'.join(list)
        List.append(ip)
    return List



def get_host_by_name(url):
    domain = urlparse(url)
    ip = socket.gethostbyname(domain.path)
    return ip

