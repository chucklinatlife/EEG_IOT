#!/usr/bin/python
# -*- coding: utf-8 -*-


#Original Author: github.com/akloster
#Changes made by: github.com/cklam19

from NeuroSkyAPI.mindwave.parser import ThinkGearParser, TimeSeriesRecorder
import bluetooth
import time
import sys
import argparse

from NeuroSkyAPI.mindwave.bluetooth_headset import connect_magic, connect_bluetooth_addr
from NeuroSkyAPI.mindwave.bluetooth_headset import BluetoothError
from NeuroSkyAPI.examples.example_startup import mindwave_startup

import socket
#variable to debug code on local side
RUN_LOCAL = False
    
#define IP address same as Intel Edison
SERVER_ADDRESS =    '192.168.43.119'

bMeasure = ['attention','meditation','blink','raw','poor_signal']
'''
0 = attention, 
1 = meditation, 
2 = blink, 
3 = raw, 
4 = poor_signal
'''
#NOTE: blink and poor_signal not yet implemented
choice = 1

description = """Simple Neurofeedback console application.

Make sure you paired the Mindwave to your computer. You need to
do that pairing for every operating system/user profile you run
seperately.

If you don't know the address, leave it out, and this program will
figure it out, but you need to put the MindWave Mobile headset into
pairing mode first.

"""

if __name__ == '__main__':

    #set const to attention. using attention value
    extra_args=[dict(name='measure', type=str, nargs='?',
            const=bMeasure[choice], default= bMeasure[choice],
            help="""Measure you want feedback on. Either "meditation" or "raw"
            or "attention\"""")]
            
    #connect to mindwave mobile
    #uses mindwave mobile API to connect headset to bluetooth adapter
    mw_socket, args = mindwave_startup(description=description,
                              extra_args=extra_args)

    #define new variable and set it to TimeSeriesRecorder from Mindwave Library
    recorder = TimeSeriesRecorder()
    #pass recorder variable into ThinkGearParser from Mindwave
    parser = ThinkGearParser(recorders=[recorder])

    #set measure_name to Attention (can also be set to meditation)
    
    if not RUN_LOCAL:
        #define an INET, STREAMing socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #define IP address and match port with EEGServer port
        server_address = (SERVER_ADDRESS,2222)
        print >>sys.stderr, 'connecting to %s port %s' % server_address
        #socket connect requires IP address and also port number
        sock.connect(server_address)
        
    while 1:
        time.sleep(0.25)
        data = mw_socket.recv(20000)
        parser.feed(data)
        
        brainSignal = getattr(recorder,args.measure)
        
        if len(brainSignal)>0:
            signalVal = brainSignal.values[-1]
            #write data in format to send to Intel Edison
            data2 = str(signalVal)+'\r\n'
            
            print "Current " + str(args.measure).upper()+ " Value", data2
            
            if not RUN_LOCAL:
                sock.sendall(data2)
                time.sleep(0.25)
           
   

