from dataclasses import dataclass


@dataclass
class Vehicle:
    speed: int = 0
    rpm: int = 0

    isSeatbelt: bool = 0
    isIndicating: bool = 0
    isChangingLane: bool = 0

    xAcceleration: float = 0.0
    zAcceleration: float = 0.0
    gpsLatitude: str = ""
    gpsLongitude: str = ""

    def collectVehicleData(self):
        # Collect 1 vehivle data... somehow
        print("Collecting 1 vehicle data")
