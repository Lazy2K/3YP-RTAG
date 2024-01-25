import serial
import sys

GPGGA = 0
NMEA = 0

ser = serial.Serial("/dev/ttyS0")
while True:
    rc = ser.readline()
    if rc.find("$GPGGA,".encode()):
        GPGGA = rc.split("$GPGGA,".encode(), 0)[0]
    print(GPGGA)
