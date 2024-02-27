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

# assets\audio\voices\katara\imkatara.mp3

# Setup alert-generator object
alertGenerator = Generator("database/alerts/alerts.db")
vehicle = Vehicle()


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
        # print(vehicle.xAcceleration)


def runAlertDetector():
    while True:
        alertDetector.run()


# We can pass threaded functions the generator object so that it can add alerts to the queue when needed


def other(generator):
    generator.registerAlert(
        Alert(alertType.SPEED_LIMIT_EXCEEDED, alertSound.SPEED_LIMIT_EXCEEDED))
    generator.registerAlert(
        Alert(alertType.LANE_CHANGE, alertSound.LANE_CHANGE))
    generator.registerAlert(
        Alert(alertType.ACCELERATION_TOO_FAST, alertSound.ACCELERATION_TOO_FAST))
    generator.registerAlert(
        Alert(alertType.DECELERATION_TOO_FAST, alertSound.DECELERATION_TOO_FAST))
    generator.registerAlert(
        Alert(alertType.CORNER_TOO_HARD, alertSound.CORNER_TOO_HARD))
    generator.registerAlert(
        Alert(alertType.SEATBELT_DISCONNECTED, alertSound.SEATBELT_DISCONNECTED))


if __name__ == "__main__":

    # imkatara.play()

    event = threading.Event()
    event.clear()

    threads = []
    threads.append(threading.Thread(target=processGeneratedAlerts))
    threads.append(threading.Thread(target=collectVehicleData))
    threads.append(threading.Thread(target=runAlertDetector))
    # threads.append(threading.Thread(target=other, args=(alertGenerator,)))

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
