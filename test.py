import serial
import sys

GPGGA = []
NMEA = []

GPGGA_look = "$GPGGA,"

ser = serial.Serial("/dev/ttyS0")
while True:
    rc = ser.readline()
    print(rc)
    da = rc.find(GPGGA_look)
    print(rc)
    if da > 0:
        GPGGA = rc.split("$GPGGA,".encode(), 1)[0]
        NMEA = GPGGA.split(",".encode())
        print(NMEA)
