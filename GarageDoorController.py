import time
from RelaisController import RelaisController
from Logger import Logger

class GarageDoorController:

    TIME_TO_TOGGLE_GARAGE = 13

    def __init__(self):
        self._log = Logger()
        self._relaisController = RelaisController()

    def toggle(self):
        self._log.info("Toggeling garagedoor")
        self._relaisController.openRelais_A() # Strom ein
        time.sleep(self.TIME_TO_TOGGLE_GARAGE)
        self._relaisController.closeRelais_A() # Strom aus


    def dispose(self):
        self._log.info("Disposing GarageDoorController...")
        self._relaisController.cleanUp()