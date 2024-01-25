import serial
import sys

ser = serial.Serial("/dev/ttyS0")
while True:
    rc = ser.read()
    dl = ser.inWaiting()
    rc += ser.read(dl)
    print(rc)
