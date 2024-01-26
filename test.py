import pynmea2
import serial
import sys


GPGGA = []
NMEA = []

GPGGA_look = "$GPGGA,"

ser = serial.Serial("/dev/ttyS0")
while True:
    rc = ser.readline()
    print(rc)
    if rc[0:5] == "$GPGGA":
        msg = pynmea2.parse(rc)
        print(msg)
