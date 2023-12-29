# Local modules -- Need to be careful of name space using import *
from modules.generator.generator import *
from modules.lanevision.lanevision import *

# Remote and standard modules
import threading

# Setup alert-generator object
alertGenerator = Generator("database/alerts/alerts.db")


def runGenerator():
    """ Docstring """

    # We never know when we'll recieve a new alert so this must always be running
    while True:  # Run checks here for any interupts or reasons to stop the generator
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
