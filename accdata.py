import busio
import digitalio
import adafruit_lis3dh
import board
import time
import csv


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


with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)

    for i in range(0, 1000):
        data = acc.collectAccData()
        writer.writerow([data.x, data.y, data.z])
