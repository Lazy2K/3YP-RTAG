# Local modules
from modules.generator.generator import *

# Remote and standard modules
import threading

# Setup alert-generator object
alertGenerator = Generator()


def runGenerator():
    while True:
        alertGenerator.processAlert()

def other():
    print("No")


if __name__ == "__main__":

    alertGenerator.registerAlert(alertType.ACCELERATION_TOO_FAST)
    alertGenerator.registerAlert(alertType.CORNER_TOO_HARD)
    alertGenerator.registerAlert(alertType.LANE_CHANGE)
    alertGenerator.registerAlert(alertType.SEATBELT_DISCONNECTED)

    t1 = threading.Thread(target=runGenerator)
    t2 = threading.Thread(target=other)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done")