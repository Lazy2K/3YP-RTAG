import serial
import sys

GPGGA = ""
NMEA = ""

ser = serial.Serial("/dev/ttyS0")
while True:
    rc = ser.readline()
    if rc.find("$GPGGA,".encode()):
        GPGGA = rc.split("$GPGGA,".encode(), 1)[1]
    print(GPGGA)
