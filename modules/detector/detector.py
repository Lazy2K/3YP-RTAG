from ..vehicle.vehicle import Vehicle


class Detector:
    def __init__(self, vehicle: Vehicle, generator):
        self.vehicle = vehicle
        self.generator = generator

    def run(self):
        if self.vehicle.zAcceleration > 0:
            print(self.vehicle.zAcceleration)
