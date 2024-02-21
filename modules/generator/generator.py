from enum import Enum
import pygame
import sqlite3
import queue


class alertType(Enum):
    """ Class Docstring """
    # Lane based alerts
    LANE_CHANGE = 1
    # Speed based alerts
    SPEED_LIMIT_EXCEEDED = 2
    # Acceleration based alerts
    ACCELERATION_TOO_FAST = 3
    DECELERATION_TOO_FAST = 4
    CORNER_TOO_HARD = 5
    # Cockpit based alerts
    SEATBELT_DISCONNECTED = 6
    LOSS_OF_TRACTION = 7


class alertSounds(Enum):
    SPEED_LIMIT_EXCEEDED = pygame.mixer.Sound(
        'assets/audio/voices/katara/imkatara.mp3')


class Alert():
    """ Class Docstring """

    def __init__(self, alertType, alertSound):
        self.alertType = alertType
        self.alertSound = alertSound


class Generator:
    """ Class Docstring """

    def __init__(self, databaseLocation):
        """ Function Docstring """
        try:
            # Hard-coding locations like this is probably not the best solution
            # Because we're defining the object in main.py so the path is from there
            # So this would completley break if an object is defined anywhere else
            self.connection = sqlite3.connect(databaseLocation).cursor()
            pygame.init()  # Initialise pygame sound mixer
        except Exception as error:
            print(error)
            raise Exception()

        self.queuedAlerts = queue.Queue()

    def registerAlert(self, alertObject):
        """ Function Docstring """
        print("Registering alert: " + str(alertObject.name))
        self.queuedAlerts.put(alertObject)
        alertObjectId = id(alertObject)
        # self.connection.execute("")

    def processAlert(self):
        """ Function Docstring """
        alertObject = self.queuedAlerts.get()
        print(alertObject.alertType)
        alertObjectId = id(alertObject)
        alertObject.alertSound.play()
        # self.connection.execute("")
        # Process alert
        # Play sound
        self.queuedAlerts.task_done()
