from dataclasses import dataclass
import pynmea2  # GPS decoder library
import serial  # UART (Rx/Tx) library
import time  # Timing library
import board  # GPIO pin auto detection library
import digitalio  # Digital GPIO library
import busio  # I2C library
import adafruit_lis3dh  # Hardware specific acceleromiter library


class HardwareInterface:
    """ Docstring """

    def __init__(self, serialPort: str = None):
        if serial == None:
            self.GPS = self.GPS("/dev/ttyS0")  # Default serial port
        else:
            self.GPS = self.GPS(serialPort)  # User defined serial port

        # self.Accelerometer = self.Accelerometer()

    class GPS:
        """ Docstring """

        def __init__(self, serialPort):
            self.GPGGA = "$GPGGA"  # Global Positioning System Fix Data
            self.serialPort = serialPort    # UART serial port
            self.serialConnection = serial.Serial(serialPort)

        def collectGpsData(self, timeoutSeconds):
            """ Docstring """
            serialLine = b''  # Empty bype array
            timeout = time.time() + timeoutSeconds
            while serialLine[0:6] != self.GPGGA.encode():
                if time.time() > timeout:
                    print("GPS timeout limit reached")
                    return None
                serialLine = self.serialConnection.readline()
                if serialLine[0:6] == self.GPGGA.encode():
                    gpsData = pynmea2.parse(serialLine.decode())
                    return gpsData

    class Accelerometer:
        """ Docstring """

        def __init__(self):
            self.I2C = busio.I2C
            self.int1 = digitalio.DigitalInOut(board.D24)
            self.acceleromiter = adafruit_lis3dh.LIS3DH_I2C(
                self.I2C, int1=self.int1)

        def collectAccData(self, timeoutSeconds):
            """ Docstring """
            print(timeoutSeconds)
            return self.acceleromiter.acceleration


@dataclass
class Vehicle:
    """ Docstring """

    # Vehicle Interface Data
    speed: int = 0
    rpm: int = 0
    isSeatbelt: bool = 0
    isIndicating: bool = 0

    # Lane Vision Data
    isInLane: bool = 0
    isChangingLane: bool = 0

    # Acceleration Data
    xAcceleration: float = 0.0  # Lateral acceleration
    zAcceleration: float = 0.0  # Forwards / backwards acceleration

    # GPS Data
    gpsLatitude: str = ""
    gpsLongitude: str = ""
    gpsQuality: float = 0.0
    satsConnected: int = 0

    def setLaneAttributes(self, inLane: bool, isChanging: bool):
        """ Docstring """
        self.isInLane = inLane
        self.isChangingLane = isChanging

    hardwareInterface = HardwareInterface("/dev/ttyS0")

    def collectVehicleData(self):
        """ Docstring """
        print("Running")
        gpsData = None  # self.hardwareInterface.GPS.collectGpsData(60)
        accData = self.hardwareInterface.Accelerometer.collectAccData(60)

        if (gpsData != None):
            self.gpsLatitude = gpsData.latitude
            self.gpsLongitude = gpsData.longitude
            self.gpsQuality = gpsData.gps_qual

        if (accData != None):
            # Figure out the correct indexes then remove this comment
            self.zAcceleration = accData[0]

        print(gpsData)
        print(accData)

        # if (accData):
        # print("Acc data goes here")
