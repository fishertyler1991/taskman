from time import time
from os import system, name
from enum import Enum

#_checkOS
# Checks the current OS and returns an snum representation.
class OS_TYPES(Enum):
    UNKNOWN = 0
    WINDOWS = 1
    UNIX = 2
    INIT = 3
_OSCAHCE = OS_TYPES.INIT

def _checkOS():
    global _OSCAHCE
    if _OSCAHCE != OS_TYPES.INIT:
        return _OSCAHCE
    else:
        osType = OS_TYPES.UNIX
        if name == 'nt':
            osType = OS_TYPES.WINDOWS
        _OSCAHCE = osType
        return osType

#_clearConsole
# Checks if the OS is using windows or not and runs the approiate command to clear the console.
def _clearConsole():
    if _checkOS() == OS_TYPES.WINDOWS:
        system('cls')
    else:
        system("clear")

#pDelta
# Simple class for controlling fps and providing a delta value for US between calls
# doFrame will be true a number of times per second equal to targetFPS
# delta will always be the time between the last two update calls
# calcFPS is the true FPS that is being acheived
# example use, the below code will print the output ~60 times every second
#   frameController = pDelta()
#   while True:
#       frameController._update()
#       if frameController.doFrame:
#           print("do main actions")
class pDelta:
    def __init__(self, setTarFPS=60.0, stopAfterSeconds=0.0):
        self._reset(setTarFPS, stopAfterSeconds)

    def _reset(self, setTarFPS, stopAfterSeconds):
        self.targetFPS = setTarFPS
        self.stopAfterSeconds = stopAfterSeconds
        self.incAmt = int(1e6 / self.targetFPS)
        self.incCount = 0
        self.doFrame = False
        self.lastUS = None
        self.startUS = None
        self.totalFrames = 0
        self.stopped = False
        self.calcFPS = self.targetFPS
        self.FPS = self.targetFPS
        self.palaDelta = -1.0

    def _setNewFPS(self, newFPS=60.0, stopAfterSeconds=0.0):
        self._reset(newFPS, stopAfterSeconds)

    def _update(self):
        curUS = int(time() * 1e6)
        self.doFrame = False

        if self.lastUS is None:
            self.startUS = curUS
            self.lastUS = curUS
            self.doFrame = True
            self.totalFrames += 1
            return

        totalTimeSec = (curUS - self.startUS) / 1e6
        if not self.stopped and self.stopAfterSeconds > 0 and totalTimeSec >= self.stopAfterSeconds:
            self.stopped = True
            return

        self.palaDelta = (curUS - self.lastUS) / 1e6
        self.incCount += curUS - self.lastUS

        if self.incCount >= self.incAmt:
            self.incCount -= self.incAmt
            self.doFrame = True
            self.totalFrames += 1

        self.lastUS = curUS

        if self.startUS is not None and totalTimeSec > 0:
            self.calcFPS = self.totalFrames / totalTimeSec
        pass
    pass