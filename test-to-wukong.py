#!/usr/bin/python
# -*- coding: utf-8 -*-


#Original Author: github.com/akloster
#Changes made by: github.com/cklam19

import time
import sys
import argparse
import socket

import random

    
#define IP address same as Gateway
SERVER_ADDRESS =    '169.234.33.113'


if __name__ == '__main__':
    
    #define an INET, STREAMing socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #define IP address and match port with EEGServer port
    server_address = (SERVER_ADDRESS,2222)
    print >>sys.stderr, 'connecting to %s port %s' % server_address
    #socket connect requires IP address and also port number
    sock.connect(server_address)

    while True:
        #time.sleep(0.25)
        
        nmin = .08
        t_end = time.time() + 60*(nmin)
        
        #append data to array for 
        while (time.time() < t_end):
                randNum = random.randrange(-1000,1000)
                sock.sendall(str(randNum))
                print(str(randNum)+'\n')
                time.sleep(0.010)
        
 
        