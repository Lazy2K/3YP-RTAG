# Local modules -- Need to be careful of name space using import *
from modules.lanevision.lanevision import *
from modules.generator.generator import *
from modules.detector.detector import *
from modules.vehicle.vehicle import *

# Remote and standard modules
import threading
import pygame
import time
import sys

# Import voice files
pygame.init()
imkatara = pygame.mixer.Sound('assets/audio/voices/katara/imkatara.mp3')


# Set up objects
vehicle = Vehicle()
alertGenerator = Generator("database/alerts/alerts.db")
alertDetector = Detector(vehicle, alertGenerator)


# THREADS
def processGeneratedAlerts():
    """ Docstring """
    while True:
        alertGenerator.processAlert()


def collectVehicleData():
    """ Docstring """
    while True:
        vehicle.collectVehicleData()


def runAlertDetector():
    while True:
        alertDetector.run()


# We can pass threaded functions the generator object so that it can add alerts to the queue when needed


if __name__ == "__main__":

    event = threading.Event()
    event.clear()

    threads = []
    threads.append(threading.Thread(target=processGeneratedAlerts))
    threads.append(threading.Thread(target=collectVehicleData))
    threads.append(threading.Thread(target=runAlertDetector))

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
