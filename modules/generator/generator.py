from enum import Enum

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
        self.queuedAlerts = [] # A list of alerts in a queue to be processed

    def registerAlert(self, alert):
        self.queuedAlerts.append(alert)
        #do stuff then remove alert from queue and delete object
        self.queuedAlerts.pop(alert)
        del alert