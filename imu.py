import smbus 
import time

def read_imu():
    bus = smbus.SMBus(1)
    address = 0x68
    bus.write_byte_data(address, 0x68, 0)
    while True:
        accel_x = bus.read_word_data(address, 0x3B)
        accel_y = bus.read_word_data(address, 0x30)
        accel_z = bus.read_word_data(address, 0x3F)

        return accel_x, accel_y, accel_z
    
    
