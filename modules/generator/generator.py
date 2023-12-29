from enum import Enum
import sqlite3
import queue
import datetime


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

    def __init__(self, databaseLocation):
        """ Function Docstring """
        try:
            # Hard-coding locations like this is probably not the best solution
            # Because we're defining the object in main.py so the path is from there
            # So this would completley break if an object is defined anywhere else
            self.connection = sqlite3.connect(
                databaseLocation, check_same_thread=False)
            self.cursor = self.connection.cursor()
            self.cursor.execute(
                "CREATE TABLE IF NOT EXISTS alerts(alertID, alertType, alertTime)")
        except Exception as error:
            print(error)
            raise Exception()

        self.queuedAlerts = queue.Queue()

    def registerAlert(self, alertObject, context=None):
        """ Function Docstring """
        self.queuedAlerts.put(alertObject)
        alertObjectId = id(alertObject)
        if context:
            print(context)
        self.cursor.execute(
            "INSERT INTO alerts (alertID, alertType, alertTime) VALUES ('" + str(alertObjectId) + "', '" + str(alertObject) + "','" + str(datetime.datetime.now()) + "')")
        self.connection.commit()

    def processAlert(self):
        """ Function Docstring """
        alertObject = self.queuedAlerts.get()
        print(alertObject)
        alertObjectId = id(alertObject)
        # self.connection.execute("")
        # Process alert
        # Play sound
        self.queuedAlerts.task_done()
