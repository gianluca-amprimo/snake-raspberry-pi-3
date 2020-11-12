import RPi.GPIO as GPIO
import spidev
import time
import os

#Open SPI bus
spi=spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

#Function for reading data
def ReadChannel(channel):
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

#assign a name to data channel
swt_channel=0
vrx_channel=1
vry_channel=2

#delay between readings in s
delay=0.05

#cyclic reading of position
while True:
    #read joystick position
    vrx_pos=ReadChannel(vrx_channel)
    vry_pos=ReadChannel(vry_channel)
    
    #read switch
    swt_val=ReadChannel(swt_channel)
    
    # Print out results
    print "--------------------------------------------"
    #print("X : {}  Y : {}  Switch : {}".format(vrx_pos,vry_pos,swt_val))
    if vrx_pos<10:
        print "left"
    elif vrx_pos==1023:
        print "right"
    if vry_pos==1023:
        print "up"
    elif vry_pos<10:
        print "down"
    if swt_val<10:
        print "switching"
       
    # Wait before repeating loop
    time.sleep(delay)


