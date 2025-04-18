class Calculation:
    def __init__(self, calculationLine):
        self.__calculationLine = calculationLine
    @property
    def GetLastSymbol(self):
        return self.__calculationLine[-1]
    @property
    def GetCalculationLine(self):
        return self.__calculationLine
    @GetCalculationLine.setter
    def SetCalculationLine(self, new_calculationLine):
        self.__calculationLine = new_calculationLine
    @GetLastSymbol.setter
    def SetLastSymbolCalculationLine(self, simbol):
        self.__calculationLine += simbol
    @GetLastSymbol.deleter
    def DeleteLastSymbol(self):
        self.__calculationLine = self.__calculationLine[:-1]
propert = Calculation("1234")
print(propert.GetLastSymbol)
print(propert.GetCalculationLine)
propert.SetCalculationLine = "1235"
print(propert.GetCalculationLine)
propert.SetLastSymbolCalculationLine = "1"
print(propert.GetCalculationLine)
print(propert.GetLastSymbol)
del propert.DeleteLastSymbol
print(propert.GetLastSymbol)
print(propert.GetCalculationLine)