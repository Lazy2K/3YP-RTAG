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
    if rc[0:6] == "$GPGGA".econde():
        print("Triggered")
        msg = pynmea2.parse(rc)
        print(msg)
