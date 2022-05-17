import serial

data = b'a'
angle = (0,0)
data1 = ((0x0000ff) & int(angle[0]*10000))
data2 = (((0x00ff00) & int(angle[0]*10000))>>8)
data3 = (((0xff0000) & int(angle[0]*10000))>>16)

data4 = ((0x0000ff) & int(angle[1]*10000))
data5 = (((0x00ff00) & int(angle[1]*10000))>>8)
data6 = (((0xff0000) & int(angle[1]*10000))>>16)

finaldata = (data1,data2,data3,data4,data5,data6)
ser = serial.Serial(port='/dev/ttyUSB0',baudrate = 9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)

while True:
    ser.write(data)
    #ser.write(finaldata)
    #ser.write(Angdata)
