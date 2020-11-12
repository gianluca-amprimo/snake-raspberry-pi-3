import RPi.GPIO as GPIO
import time

zero='1111110'
one= '0110000'
two= '1101101'
three='1111001'
four= '0110011'
five='1011011'
six='1011111'
seven='1110000'
eight='1111111'
nine='1111011'

numbers= [zero, one, two, three, four, five, six, seven, eight, nine]

a=13
b=6
c=16
d=20
e=21
f=19
g=26

pins=[a, b, c, d, e, f, g]

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(a, GPIO.OUT)
    GPIO.setup(b, GPIO.OUT)
    GPIO.setup(c, GPIO.OUT)
    GPIO.setup(d, GPIO.OUT)
    GPIO.setup(e, GPIO.OUT)
    GPIO.setup(f, GPIO.OUT)
    GPIO.setup(g, GPIO.OUT)
    
def counter(timescale):
    while True:
        for num in numbers:
            for pin, level in zip(pins, num):
                GPIO.output(pin, int(level))
            time.sleep(timescale)

if __name__=='__main__':
    setup()    
    try:        
        t=float(raw_input('Select the # s before counter update: '))
        counter(t)
    except KeyboardInterrupt:
        for pin in pins:
                GPIO.output(pin, GPIO.LOW)
        GPIO.cleanup()