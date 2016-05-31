#!/usr/bin/python
# -*- coding: utf-8 -*-


#Original Author: github.com/akloster
#Changes made by: github.com/cklam19

from NeuroSkyAPI.mindwave.parser import ThinkGearParser, TimeSeriesRecorder
from NeuroSkyAPI.mindwave.pyeeg import bin_power
import bluetooth
import time
import sys
import argparse


from NeuroSkyAPI.mindwave.bluetooth_headset import connect_magic, connect_bluetooth_addr
from NeuroSkyAPI.mindwave.bluetooth_headset import BluetoothError
from NeuroSkyAPI.examples.example_startup import mindwave_startup

import socket

    
#define IP address same as Gateway
SERVER_ADDRESS =    '169.234.33.113'

bMeasure = ['attention','meditation','blink','raw','poor_signal']
'''
0 = attention, 
1 = meditation, 
2 = blink, 
3 = raw, 
4 = poor_signal
'''
#NOTE: blink and poor_signal not yet implemented
choice = 3

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
    extra_args=[dict(name='measure', type=str, nargs='?', const=bMeasure[choice], default= bMeasure[choice], help="""Measure you want feedback on. Either "meditation" or "raw" or "attention\"""")]
    print('Remember to turn on bluetooth and turn off thinkgear connector')
    #connect to mindwave mobile
    #uses mindwave mobile API to connect headset to bluetooth adapter
    mw_socket, args = mindwave_startup(description=description,
                              extra_args=extra_args)
    #define new variable and set it to TimeSeriesRecorder from Mindwave Library
    recorder = TimeSeriesRecorder()
    #pass recorder variable into ThinkGearParser from Mindwave
    parser = ThinkGearParser(recorders=[recorder])

    #define an INET, STREAMing socket
    #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #define IP address and match port with EEGServer port
    #server_address = (SERVER_ADDRESS,2222)
    #print >>sys.stderr, 'connecting to %s port %s' % server_address
    #socket connect requires IP address and also port number
    #sock.connect(server_address)
    '''
    recording time
    t_end = time.time() + 60*(nmin)
    
    #loop until time over
    while time.time() < t_end :
    '''
    eyesOpen = False
    count = 0
    print_once = True
    start_time = time.time()
    while True:
        brainArray = []
        time.sleep(0.25)
        
        nmin = .08
        t_end = time.time() + 60*(nmin)
        #start_time = time.time()
        if count < 40:
            #append data to array for 
            while (time.time() < t_end):
                data = mw_socket.recv(20000)
                parser.feed(data)
                brainSignal = getattr(recorder,args.measure)
                if len(brainSignal)>0:
                    signalVal = brainSignal.values[-1]
                    #append data to brainArray
                    brainArray.append(signalVal)
                    #write data in format to send pver socket
                    #data2 = str(signalVal)+'\r\n'
                    data2 = str(signalVal)
                    print "Current " + str(args.measure).upper()+ " Value " + data2
                    
                   
                    #sock.sendall(data2)
                    #time.sleep(0.25)
            
            brainArraySpectrum, brainArrayRelSpectrum = bin_power(brainArray,[0.5,4,7,12,30],512)
            
            if eyesOpen == False:
                eyetag = '0'
            else:
                eyetag = '1'
            
            with open('brainArray-data.txt','a') as f:
                f.write(eyetag + ' ' + ' '.join(map(str,brainArray)) + '\n')
             
            with open('brainArray-data-spectrum.txt','a') as f:
                f.write(eyetag + ' ' + ' '.join(map(str,brainArraySpectrum)) + '\n')
            
            with open('brainArray-data-relspectrum.txt','a') as f:
                f.write(eyetag + ' ' + ' '.join(map(str,brainArrayRelSpectrum)) + '\n')
         
            count = count + 1
            print('------------------------'+str(count))
        end_time = time.time() - start_time
        if count == 40 and print_once:
            print('---------------------')
            print(end_time)
            print_once = not print_once
'''
        userInput = raw_input('change eyetag?\n')
        if userInput == 'y':
            eyesOpen = not eyesOpen
            print('eyes open: ' + str(eyesOpen) + '\n')
        else:
            print('eyes open: ' + str(eyesOpen) + '\n')
        '''
'''
        if len(recorder.raw)>=500:
			spectrum, relative_spectrum = bin_power(recorder.raw[-512*3:],[0.5,4,7,12,30],1024)
            #print(int(round(time.time() * 1000)))
			
			#split data received
			spectrum_splitted = str(spectrum).split()
			
			#grab alpha data
			#need to verify alpha waves
			#deltaData = spectrum_splitted[1]

			alphaData = spectrum_splitted[3]
			
			#print to console
			print(spectrum_splitted[3])
			print('---------------')
			
			#print to file
			with open('binPower-alphaData.txt','a') as f:
				f.write(str(spectrum_splitted[3])+'\n')
	

            with open('datafile2.txt','a') as f:
                f.write(str(relative_spectrum)+'\n')
'''






        