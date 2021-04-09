import time
import board
import busio
import adafruit_bme280

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25

# Temperature in Fahrenheit
tempVal = bme280.temperature*1.8 +32

# Humidity 
humiVal = bme280.relative_humidity

# Altitude in feet
altiVal = bme280.altitude*3.281

while True:
    file = open("/home/spring2021/Desktop/Gnu radio code/backup2/File_recevie_send/Txt_sent.txt","w+")
    file.write("Temperature: %0.1f F\n" % tempVal)
    file.write("Humidity: %0.1f %%\n" % humiVal)
    file.write("Altitude: %0.2f ft" % altiVal)
  
    print("Sensor Information Recorded")
    time.sleep(2)
