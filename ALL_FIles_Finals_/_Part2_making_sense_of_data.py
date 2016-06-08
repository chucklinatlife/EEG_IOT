import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys,string
from pylab import *
from pyeeg import bin_power
import glob
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
%matplotlib inline
##################### This file to generating all the features from bin_power###################
#here split the data to eyeclose and eyeopen from the raw data 
chunkList = []
with open('eyeclose.txt', 'r') as fc:
    datalist = fc.readlines()
    for line in datalist:
        x= line.split("\n")
        del x[-1]
        chunkList.append(x)
dataListArray = []
for k in chunkList:
    dataList = str(k).replace('[','').replace(']','').replace('\'','').split(' ')
    dataListArray.append(dataList)
for j in range(len(dataListArray)):
    for i in range(len(dataListArray[j])):
        filePath = 'EEG\eyeclose\Teyeclose' + str(j+1) + '.txt'
        with open (filePath,'a') as f:
            f.write(dataListArray[j][i]+'\n')

chunkList1 = []
with open('eyeopen.txt', 'r') as fo:
    datalist1 = fo.readlines()
    for line in datalist1:
        x= line.split("\n")
        del x[-1]
        chunkList1.append(x)
dataListArray1 = []
for k1 in chunkList1:
    dataList1 = str(k1).replace('[','').replace(']','').replace('\'','').split(' ')
    dataListArray1.append(dataList1)
for j in range(len(dataListArray1)):
    for i in range(len(dataListArray1[j])):
        filePath = 'EEG\eyeopen\Teyeopen' + str(j+1) + '.txt'
        with open (filePath,'a') as fo:
            fo.write(dataListArray1[j][i]+'\n')
			
			
			
# here generating the feature using bin_power function for generationg and extracting Alpha signal
with open('resultc3.txt','a') as resultc:
    for i in range(40):
        X = open("EEG\eyeclose\Teyeclose"+str(i+1)+".txt","r")
        power , power_ratio = bin_power(list(X)[-512*3:],[0.5,4,7,12,30], 1024)
        signal_splitted =str(power).split()
        alpha_Signal = signal_splitted[3]
        resultc.write(str(alpha_Signal)+'\n')

with open('resulto3.txt', 'a') as resulto:
    for i in range(40):
        X = open("EEG\eyeopen\Teyeopen" + str(i + 1) + ".txt", "r")
        power, power_ratio = bin_power(list(X)[-512 * 3:], [0.5, 4, 7, 12, 30], 1024)
        signal_splitted = str(power).split()
        alpha_Signal = signal_splitted[3]
        resulto.write(str(alpha_Signal) + '\n')

with open('resultc2.txt','a') as resultc:
    for i in range(40):
        X = open("EEG\eyeclose\Teyeclose"+str(i+1)+".txt","r")
        power , power_ratio = bin_power(list(X)[-512*3:],[0.5,4,7,12,30], 1024)
        signal_splitted =str(power).split()
        alpha_Signal = signal_splitted[2]
        resultc.write(str(alpha_Signal)+'\n')

with open('resulto2.txt', 'a') as resulto:
    for i in range(40):
        X = open("EEG\eyeopen\Teyeopen" + str(i + 1) + ".txt", "r")
        power, power_ratio = bin_power(list(X)[-512 * 3:], [0.5, 4, 7, 12, 30], 1024)
        signal_splitted = str(power).split()
        alpha_Signal = signal_splitted[2]
        resulto.write(str(alpha_Signal) + '\n')

with open('resultc1.txt','a') as resultc:
    for i in range(40):
        X = open("EEG\eyeclose\Teyeclose"+str(i+1)+".txt","r")
        power , power_ratio = bin_power(list(X)[-512*3:],[0.5,4,7,12,30], 1024)
        signal_splitted =str(power).split()
        alpha_Signal = signal_splitted[1]
        resultc.write(str(alpha_Signal)+'\n')

with open('resulto1.txt', 'a') as resulto:
    for i in range(40):
        X = open("EEG\eyeopen\Teyeopen" + str(i + 1) + ".txt", "r")
        power, power_ratio = bin_power(list(X)[-512 * 3:], [0.5, 4, 7, 12, 30], 1024)
        signal_splitted = str(power).split()
        alpha_Signal = signal_splitted[1]
        resulto.write(str(alpha_Signal) + '\n')
In [40]:
# here generating the feature using bin_power function for generationg and extracting Alpha signal
with open('resultc4.txt','a') as resultc:
    for i in range(40):
        X = open("EEG\eyeclose\Teyeclose"+str(i+1)+".txt","r")
        power , power_ratio = bin_power(list(X)[-512*3:],[0.5,4,7,12,30], 1024)
        signal_splitted =str(power).split()
        alpha_Signal = signal_splitted[4]
        resultc.write(str(alpha_Signal)+'\n')

with open('resulto4.txt', 'a') as resulto:
    for i in range(40):
        X = open("EEG\eyeopen\Teyeopen" + str(i + 1) + ".txt", "r")
        power, power_ratio = bin_power(list(X)[-512 * 3:], [0.5, 4, 7, 12, 30], 1024)
        signal_splitted = str(power).split()
        alpha_Signal = signal_splitted[4]
        resulto.write(str(alpha_Signal) + '\n')
#################################################################
#here the machine learning Algorithim started . 
#delta....
open_ds1 = pd.read_csv("resulto1.txt")
close_ds1 = pd.read_csv("resultc1.txt")

#again this is for me , it is not important for the final code 
#This is to plot the points
plt.scatter(open_ds1.index, open_ds1, c="red")
plt.scatter(close_ds1.index, close_ds1, c="blue")
################################################################
#here the machine learning Algorithim started . 
#theta....
open_ds2 = pd.read_csv("resulto2.txt")
close_ds2 = pd.read_csv("resultc2.txt")
#again this is for me , it is not important for the final code 
#This is to plot the points
plt.scatter(open_ds2.index, open_ds2, c="red")
plt.scatter(close_ds2.index, close_ds2, c="blue")
################################################################
#here the machine learning Algorithim started . 
#alpha .....
open_ds3 = pd.read_csv("resulto3.txt")
close_ds3 = pd.read_csv("resultc3.txt")
#again this is for me , it is not important for the final code 
#This is to plot the points
plt.scatter(open_ds3.index, open_ds3, c="red")
plt.scatter(close_ds3.index, close_ds3, c="blue")
##################################################################
#here the machine learning Algorithim started . 
#beta .... 
open_ds4 = pd.read_csv("resulto4.txt")
close_ds4 = pd.read_csv("resultc4.txt")
#again this is for me , it is not important for the final code 
#This is to plot the points
plt.scatter(open_ds4.index, open_ds4, c="red")
plt.scatter(close_ds4.index, close_ds4, c="blue")
##################################################################

