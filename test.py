import serial
import sys

ser = serial.Serial("/dev/ttyS0")
while True:
    rc = ser.readline()
    print(rc)
