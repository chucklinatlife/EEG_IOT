#!/usr/bin/python
# -*- coding: utf-8 -*-

from mindwave.parser import ThinkGearParser, TimeSeriesRecorder
import bluetooth
import time
import sys
import argparse
from progressbar import ProgressBar, Bar, Percentage


from mindwave.bluetooth_headset import connect_magic, connect_bluetooth_addr
from mindwave.bluetooth_headset import BluetoothError
from example_startup import mindwave_startup

import socket
import sys
from time import sleep



description = """Simple Neurofeedback console application.

Make sure you paired the Mindwave to your computer. You need to
do that pairing for every operating system/user profile you run
seperately.

If you don't know the address, leave it out, and this program will
figure it out, but you need to put the MindWave Mobile headset into
pairing mode first.

"""
if __name__ == '__main__':

    extra_args=[dict(name='measure', type=str, nargs='?',
            const="attention", default="attention",
            help="""Measure you want feedback on. Either "meditation"
            or "attention\"""")]
    mw_socket, args = mindwave_startup(description=description,
                              extra_args=extra_args)

    if args.measure not in ["attention", "meditation"]:
        print "Unknown measure %s" % repr(args.measure)
        sys.exit(-1)
    recorder = TimeSeriesRecorder()
    parser = ThinkGearParser(recorders=[recorder])

    if args.measure== 'attention':
        measure_name = 'Attention'
    else:
        measure_name = 'Meditation'

    #bar = ProgressBar(widgets=[measure_name, Percentage(), Bar()]).start()
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('192.168.43.119',2222)
    print >>sys.stderr, 'connecting to %s port %s' % server_address
    sock.connect(server_address)
    
    while 1:
        time.sleep(0.25)
        data = mw_socket.recv(20000)
        parser.feed(data)
        v = 0
        if args.measure == 'attention':
            if len(recorder.attention)>0:
                v = recorder.attention[-1]
                #print('Current Attention Value:',recorder.attention.values[-1])
                attentionVal = recorder.attention.values[-1]
                data2 = str(attentionVal)+'\r\n'
                print "Current Attention Value", data2
                sock.sendall(data2)
                sleep(0.5)
                
        if args.measure == 'meditation':
            if len(recorder.meditation)>0:
                v = recorder.meditation[-1]
        if v>0:
            #print "result is: %s" %(v)
            #bar.start()
            #bar.update(v)
            #print "v > 0"
			pass

