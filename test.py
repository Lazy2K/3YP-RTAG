import serial
import sys

GPGGA = ""
NMEA = ""

ser = serial.Serial("/dev/ttyS0")
while True:
    rc = ser.readline()
    if rc.find("$GPGGA"):
        GPGGA = rc.split("$GPGGA,", 1)[1]
    print(GPGGA)
