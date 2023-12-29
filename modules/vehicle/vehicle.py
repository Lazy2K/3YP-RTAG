from dataclasses import dataclass


@dataclass
class Vehicle:
    speed: int = 0
    rpm: int = 0

    isSeatbelt: bool = False
    isIndicating: bool = False
    isChangingLane: bool = False

    xAcceleration: float = 0.0
    zAcceleration: float = 0.0
    gpsLatitude: str = ""
    gpsLongitude: str = ""
