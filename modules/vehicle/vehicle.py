from dataclasses import dataclass


@dataclass
class Vehicle:
    speed: int
    rpm: int

    isSeatbelt: bool
    isIndicating: bool
    isChangingLane: bool

    x-acceleration: float
    z-acceleration: float
    gps-latitude: str
    gps-longitude: str
