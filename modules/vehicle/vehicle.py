from dataclasses import dataclass
import pynmea2
import serial
import time


class HardwareInterface:
    def __init__(self, serialPort: str = None):
        if serial == None:
            self.GPS = self.GPS("/dev/ttyS0")  # Default serial port
        else:
            self.GPS = self.GPS(serialPort)  # User defined serial port

    class GPS:
        def __init__(self, serialPort):
            self.GPGGA = "$GPGGA,"  # Global Positioning System Fix Data
            self.serialPort = serialPort    # UART serial port
            self.serialConnection = serial.Serial(serialPort)

        def collectGpsData(self, timeoutSeconds):
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
        def __init__(self):
            pass


@dataclass
class Vehicle:

    # Vehicle Interface Data
    speed: int = 0
    rpm: int = 0
    isSeatbelt: bool = 0
    isIndicating: bool = 0

    # Lane Vision Data
    isInLane: bool = 0
    isChangingLane: bool = 0

    # Acceleration Data
    xAcceleration: float = 0.0
    zAcceleration: float = 0.0

    # GPS Data
    gpsLatitude: str = ""
    gpsLongitude: str = ""
    gpsQuality: float = 0.0

    def collectVehicleData(self):
        # Collect 1 vehivle data... somehow
        print("Collecting 1 vehicle data")
        hi = HardwareInterface("/dev/ttyS0")
        print(hi.GPS.collectGpsData(60))
