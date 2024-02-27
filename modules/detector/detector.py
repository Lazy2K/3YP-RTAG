from ..vehicle.vehicle import Vehicle
from ..generator.generator import Generator
from ..generator.generator import Alert, alertType, alertSound


class Detector:
    def __init__(self, vehicle: Vehicle, generator: Generator):
        self.vehicle = vehicle
        self.generator = generator

    def run(self):
        print(self.vehicle.xAcceleration)
        if self.vehicle.xAcceleration > 0.5:
            self.generator.registerAlert(
                Alert(alertType.ACCELERATION_TOO_FAST, alertSound.ACCELERATION_TOO_FAST))
