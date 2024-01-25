import serial
import sys

GPGGA = 0
NMEA = 0

ser = serial.Serial("/dev/ttyS0")
while True:
    rc = ser.readline()
    da = rc.find("$GPGGA,".encode())
    print(da)
    if da > 0:
        GPGGA = rc.split("$GPGGA,".encode(), 1)[0]
        NMEA = GPGGA.split(",".encode())
        print(NMEA)
