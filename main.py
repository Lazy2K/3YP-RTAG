from modules.generator.generator import *

gen = Generator()

al = Alert(alertType.ACCELERATION_TOO_FAST)
gen.registerAlert(al)