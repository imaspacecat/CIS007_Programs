class Stock:
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    def getName(self):
        return self.__name

    def getSymbol(self):
        return self.__symbol

    def getPreviousClosingPrice(self):
        return self.__previousClosingPrice

    def setPreviousClosingPrice(self, price):
        self.__previousClosingPrice = price

    def getCurrentPrice(self):
        return self.__currentPrice

    def setCurrentPrice(self, price):
        self.__currentPrice = price

    def getChangePercent(self):
        return ((self.__currentPrice - self.__previousClosingPrice) / self.__previousClosingPrice) * 100

stock = Stock("INTC", "Intel Corporation", 20.5, 20.35)

print(stock.getChangePercent())