# Local modules
from modules.generator.generator import *

# Remote and standard modules
import threading

# Setup alert-generator object
alertGenerator = Generator()


def runGenerator():
    """ Docstring """
    
    while True: # We never know when we'll recieve a new alert so this must always be running
        alertGenerator.processAlert()

def other():
    print("No")


if __name__ == "__main__":

    alertGenerator.registerAlert(alertType.ACCELERATION_TOO_FAST)
    alertGenerator.registerAlert(alertType.CORNER_TOO_HARD)
    alertGenerator.registerAlert(alertType.LANE_CHANGE)
    alertGenerator.registerAlert(alertType.SEATBELT_DISCONNECTED)

    threads = []
    # Run alert generator module
    threads.append(threading.Thread(target=runGenerator))
    # Run lane detection module
    threads.append(threading.Thread(target=other))
    # Run speed detection module
    # Run accelatomiter detection module

    # Begin all threads
    for thread in threads:
        thread.start()
    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print("Done")