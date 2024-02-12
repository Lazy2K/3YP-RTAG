# Local modules -- Need to be careful of name space using import *
from modules.lanevision.lanevision import *
from modules.generator.generator import *
from modules.detector.detector import *
from modules.vehicle.vehicle import *

# Remote and standard modules
from playsound import playsound
import threading
import time
import sys

# Import voice files
imkatara = 'assets/audio/voices/katara/imkatara.mp3'

# Setup alert-generator object
alertGenerator = Generator("database/alerts/alerts.db")
vehicle = Vehicle()


def processGeneratedAlerts():
    """ Docstring """
    while True:
        alertGenerator.processAlert()


def collectVehicleData():
    """ Docstring """
    while True:
        vehicle.collectVehicleData()

# We can pass threaded functions the generator object so that it can add alerts to the queue when needed


def other(generator):
    generator.registerAlert(alertType.SPEED_LIMIT_EXCEEDED)


if __name__ == "__main__":

    playsound(imkatara)

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

    # Wait for all threads to finish
    for thread in threads:
        thread.join()
        print("Stopped: " + thread.name)

    print("Exiting program gracefully")
    # print(alertGenerator.queuedAlerts)
