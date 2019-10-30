#! /bin/usr/env python3
#
# Author: incidrhreat@hackmethod.com
# 
# Purpose:      This server is setup to listen for ICMP connections 
#               and print the data 
# 


import socket, sys

def recv():
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    while True:

        data, src = s.recvfrom(1508)
        payload = data[45:54]                   # receives hexconverted data  
        x = payload.decode().rstrip("/")        # decodes and strips "/" and assigns to 'x'
        print(chr(int(x, 2)))                   # prints ascii to screen as it's received

if __name__ == "__main__":
    recv()
