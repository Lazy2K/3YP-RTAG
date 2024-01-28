from dataclasses import dataclass
import serial


class HardwareInterface:
    def __init__(self, serial: str = None):
        if serial == None:
            self.GPS = self.GPS("/dev/ttyS0")  # Default serial port
        else:
            self.GPS = self.GPS(serial)  # User defined serial port

    class GPS:
        def __init__(self, serial):
            self.GPGGA = "$GPGGA,"  # Global Positioning System Fix Data
            self.serial = serial    # UART serial port
            self.serialConnection = serial.Serial(self.serial)

        def collectGpsData():
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
