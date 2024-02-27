from ..vehicle.vehicle import Vehicle
from ..generator.generator import Generator
from ..generator.generator import Alert, alertType, alertSound

import time


class Detector:
    def __init__(self, vehicle: Vehicle, generator: Generator):
        self.vehicle = vehicle
        self.generator = generator

        self.timeOutSeconds = 5.0
        self.timeTillNext = {  # This seems like a bad solution and inefficient
            "LANE_CHANGE": time.time(),
            "SPEED_LIMIT_EXCEEDED": time.time(),
            "ACCELERATION_TOO_FAST": time.time(),
            "DECELERATION_TOO_FAST": time.time(),
            "CORNER_TOO_HARD": time.time(),
            "SEATBELT_DISCONNECTED": time.time()
        }

    def run(self):

        print(self.vehicle.zAcceleration)
        if self.vehicle.zAcceleration > 0.5 and self.timeTillNext["ACCELERATION_TOO_FAST"] < time.time():
            # Set cooldown timer
            self.timeTillNext["ACCELERATION_TOO_FAST"] = time.time(
            ) + self.timeOutSeconds
            print("TIMETILL: " + self.timeTillNext["ACCELERATION_TOO_FAST"])
            print("TIMENOW: " + time.time())
            self.generator.registerAlert(
                Alert(alertType.ACCELERATION_TOO_FAST, alertSound.ACCELERATION_TOO_FAST))
