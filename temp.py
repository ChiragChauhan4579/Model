from smbus2 import SMBus
from mlx90614 import MLX90614

bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)
print("Object Temperature :", sensor.get_obj_temp())
with open('/home/pi/Desktop/Model/temperature.txt', 'w') as f:
    f.write(sensor.get_obj_temp())
bus.close()