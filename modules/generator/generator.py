from enum import Enum
import queue

class alertType(Enum):
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
    def __init__(self, alertType):
        self.alertType = alertType

class Generator:
    def __init__(self):
        self.queuedAlerts = queue.Queue()

    def registerAlert(self, alertObject):
        self.queuedAlerts.put(alertObject)

    def processAlert(self):
        alert = self.queuedAlerts.get()
        print(alert)
        self.queuedAlerts.task_done()