import time
import board
import busio
import adafruit_adxl34x

i2c = busio.I2C()
accelerometer = adafruit_adxl34x.ADXL345(i2c)

# while True:
# print("%f %f %f" % accelerometer.acceleration)
# time.sleep(0.5)
