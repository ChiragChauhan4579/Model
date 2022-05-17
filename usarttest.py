import time
import serial

pAzAngle = 0.0
pElAngle = 0.0
ser = serial.Serial(port='/dev/ttyUSB0',baudrate = 9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
# a = b'Hello'
def angleData():
    #i = ord(i)
    #print(i)
    sRead = ord(ser.read())
    if sRead == ord('a'):
        global pAzAngle
        b = ser.read()
        pAzAngle = ord(b)
        b = ser.read()
        pAzAngle += (ord(b)<<8)
        pAzAngle /= 10
        print(pAzAngle)
    elif sRead == ord('e'):
        global pElAngle
        b = ser.read()
        pElAngle = ord(b)
        b = ser.read()
        pElAngle += (ord(b)<<8)
        pElAngle /= 10
        print(pElAngle)    
    
while 1:
    angleData()
    #print(pAzAngle, pElAngle)
