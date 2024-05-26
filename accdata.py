import busio
import digitalio
import adafruit_lis3dh
import board
import time


class Accelerometer:
    """ Docstring """

    def __init__(self):
        self.I2C = busio.I2C(board.SCL, board.SDA)
        self.int1 = digitalio.DigitalInOut(board.D24)
        self.acceleromiter = adafruit_lis3dh.LIS3DH_I2C(
            self.I2C, int1=self.int1)

    def collectAccData(self):
        return self.acceleromiter.acceleration


acc = Accelerometer()

for i in range(0, 1000):
    print(acc.collectAccData().x)
