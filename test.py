import pynmea2
import serial
import sys


GPGGA = []
NMEA = []

GPGGA_look = "$GPGGA,"

ser = serial.Serial("/dev/ttyS0")
while True:
    rc = ser.readline()
    if rc[0:6] == "$GPRMC":
        msg = pynmea2.parse(rc)
        print(msg)
    if da > 0:
        GPGGA = rc.split("$GPGGA,".encode(), 1)[0]
        NMEA = GPGGA.split(",".encode())
        print(NMEA)
