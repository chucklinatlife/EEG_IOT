from NeuroPy import NeuroPy
import time

eyesOption = ['eyes_open','eyes_closed']
alphaOption = ['lowAlpha','highAlpha']

object1=NeuroPy("COM3") #If port not given 57600 is automatically assumed
                        #object1=NeuroPy("/dev/rfcomm0") for linux
						
'''
def attention_callback(attention_value):
    "this function will be called everytime NeuroPy has a new value for attention"
    print "Value of attention is",attention_value
    #do other stuff (fire a rocket), based on the obtained value of attention_value
    #do some more stuff
    return None
'''


#for each callback, store value into textfile
def highalpha_callback(highAlpha_value):
	print "Value of highAlpha is ", highAlpha_value
	
	file_name = str(eyesOption[0]) + '-' + str(alphaOption[1])
	with open (file_name,'a') as f:
		f.write(str(highAlpha_value)+ '\n')
		
def lowalpha_callback(lowAlpha_value):
	print "Value of lowAlpha is ", lowAlpha_value
	
	file_name = str(eyesOption[0]) + '-' + str(alphaOption[0])
	with open(file_name,'a') as f:
		f.write(str(lowAlpha_value) + '\n')

'''    
def blinkstrength_callback(blinkstrength_value):
    print "Value of blinkstrength is", blinkstrength_value
    return None
'''

#set recording timer in minutes
nmin = 1	
	
#set call back:
#object1.setCallBack("attention",attention_callback)
#object1.setCallBack("blinkStrength",blinkstrength_callback)
object1.setCallBack("highAlpha", highalpha_callback)
object1.setCallBack("lowAlpha", lowalpha_callback)


#call start method
object1.start()

t_end = time.time() + 60*(nmin)
print('start recording')

while time.time() < t_end:
	#keep running until t_end
	continue
print('done recording')