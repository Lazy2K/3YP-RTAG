from enum import Enum
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


class Alert():
    """ Class Docstring """

    def __init__(self, alertType):
        self.alertType = alertType


class Generator:
    """ Class Docstring """

    def __init__(self):
        """ Function Docstring """
        try:
            # Hard coding locations like this is probably not the best solution
            # Because we're defining the object in main.py so the path is from there
            # So this would completley break if an object is defined anywhere else
            connection = sqlite3.connect("database/alerts/alerts.db").cursor()
            connection.execute("")
        except Exception as error:
            print(error)

        self.queuedAlerts = queue.Queue()

    def registerAlert(self, alertObject):
        """ Function Docstring """
        self.queuedAlerts.put(alertObject)

    def processAlert(self):
        """ Function Docstring """
        alert = self.queuedAlerts.get()
        print(alert)
        self.queuedAlerts.task_done()
