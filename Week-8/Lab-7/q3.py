import time

class StopWatch:
    def __init__(self):
        self.__startTime = time.time()
        self.__endTime = self.__startTime

    def getStartTime(self):
        return self.__startTime

    def getEndTime(self):
        return self.__endTime

    def start(self):
        self.__startTime = time.time()

    def stop(self):
        self.__endTime = time.time()

    def getElapsedTime(self):
        return (self.__endTime - self.__startTime) * 1000

sum = 0
stopWatch = StopWatch()
stopWatch.start()
for i in range(1_000_000):
    sum += i

stopWatch.stop()
print(stopWatch.getElapsedTime())
