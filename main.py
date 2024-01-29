# Local modules -- Need to be careful of name space using import *
from modules.lanevision.lanevision import *
from modules.generator.generator import *
from modules.detector.detector import *
from modules.vehicle.vehicle import *

# Remote and standard modules
import threading
import time
import sys

# Setup alert-generator object
alertGenerator = Generator("database/alerts/alerts.db")
vehicle = Vehicle()


def processGeneratedAlerts():
    """ Docstring """
    while True:
        alertGenerator.processAlert()
        if event.is_set:
            break


def collectVehicleData():
    """ Docstring """
    while True:
        print("Getting vehicle data")
        vehicle.collectVehicleData()
        print("Vehicle data collected")
        print(vehicle)
        print("Vehicle printed")
        if event.is_set:
            break

        print("Passed the break")

# We can pass threaded functions the generator object so that it can add alerts to the queue when needed


def other(generator):
    generator.registerAlert(alertType.SPEED_LIMIT_EXCEEDED)


if __name__ == "__main__":

    event = threading.Event()
    event.clear()

    threads = []
    threads.append(threading.Thread(target=processGeneratedAlerts))
    threads.append(threading.Thread(target=collectVehicleData))
    threads.append(threading.Thread(target=other, args=(alertGenerator,)))

    # Begin all threads
    for thread in threads:
        print("Starting: " + thread.name)
        thread.start()

    while True:
        try:
            time.sleep(0.1)
        except KeyboardInterrupt:
            event.set()
            break

    # Wait for all threads to finish
    for thread in threads:
        thread.join()
        print("Stopped: " + thread.name)

    print("Exiting program gracefully")
    # print(alertGenerator.queuedAlerts)
