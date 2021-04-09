import time
import serial
import pynmea2
import string


ser = serial.Serial('./dev/ttyTHS1', 115200, timeout = 0.2)
while True:
    line = ser.readline()
    line = str(line, encoding = 'utf-8')
    if line.startswith('$GPRMC'):
        rmc = pynmea2.parse(line)
        print('Latitude:', rmc.latitude)
        print('Longitude:', rmc.longitude)
        print('Speed:', rmc.spd_over_grnd*1.85)
        
    if line.startswith('$GPGGA'):
        rmc2 = pynmea2.parse(line)
        print('Sats:', rmc2.num_sats)
    with open('getGps.txt', "a+") as file:
        file.write(line.strip())
        file.write("\n")
        file.close()

