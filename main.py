# Local modules
from modules.generator.generator import *

# Remote and standard modules
import threading

# Setup alert-generator object
alertGenerator = Generator()

# Live vehivce data
physicalVehicleData = {
    "speed": 0,
    "rmp": 0,
    "indicator": False
}

telematicVehicleData = {
    "x-accelaration": 0,
    "z-accelaration": 0
}


def runGenerator():
    """ Docstring """

    while True:  # We never know when we'll recieve a new alert so this must always be running
        alertGenerator.processAlert()


# We can pass threaded functions the generator object so that it can add alerts to the queue when needed
def other(generator):
    print("No")
    generator.registerAlert(alertType.SPEED_LIMIT_EXCEEDED)


def runVehicleDataModule():
    print(".")


def runLaneDetectionModule():
    print(".")


def runAcceleromiterModule():
    print(".")


if __name__ == "__main__":

    threads = []
    # Run alert generator module
    threads.append(threading.Thread(target=runGenerator))
    # Run lane detection module
    threads.append(threading.Thread(target=other, args=(alertGenerator,)))
    # Run speed detection module
    # Run accelatomiter detection module

    # Begin all threads
    for thread in threads:
        thread.start()
    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print("Done")
    # print(alertGenerator.queuedAlerts)
