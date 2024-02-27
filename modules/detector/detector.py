from ..vehicle.vehicle import Vehicle
from ..generator.generator import Generator
from ..generator.generator import Alert, alertType, alertSound

import time


class Detector:
    def __init__(self, vehicle: Vehicle, generator: Generator):
        self.vehicle = vehicle
        self.generator = generator

        self.xAccelerationThreashold = 1.0
        self.zAccelerationThreashold = 1.0

        self.timeOutSeconds = 10.0
        self.timeTillNext = {  # This seems like a bad solution and inefficient
            "LANE_CHANGE": time.time(),
            "SPEED_LIMIT_EXCEEDED": time.time(),
            "ACCELERATION_TOO_FAST": time.time(),
            "DECELERATION_TOO_FAST": time.time(),
            "CORNER_TOO_HARD": time.time(),
            "SEATBELT_DISCONNECTED": time.time()
        }

    def run(self):
        if self.vehicle.xAcceleration > self.xAccelerationThreashold and self.timeTillNext["ACCELERATION_TOO_FAST"] < time.time():
            # Set cooldown timer
            self.timeTillNext["ACCELERATION_TOO_FAST"] = time.time(
            ) + self.timeOutSeconds
            self.generator.registerAlert(
                Alert(alertType.ACCELERATION_TOO_FAST, alertSound.ACCELERATION_TOO_FAST))
