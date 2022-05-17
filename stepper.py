import serial
mask = open("/home/pi/Desktop/Model/mask.txt","r")
print(mask.read())
temp = open("/home/pi/Desktop/Model/temperature.txt","r")
print(temp.read())

ser = serial.Serial(port='/dev/ttyUSB0',baudrate = 9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
min_temp = '38'
flag = b'a'
if mask == 'Without Mask':
	flag = b'a'
else:
	if str(temp) < min_temp:
		flag = b'b'
ser.write(flag)
