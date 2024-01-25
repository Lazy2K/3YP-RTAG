import serial
import sys

ser = serial.Serial("/dev/ttyS0", 9600)
while True:
    rc = ser.read()
    dl = ser.in_waiting()
    rc = ser.read(dl)
    print(rc)
