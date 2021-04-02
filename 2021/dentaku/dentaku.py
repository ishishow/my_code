class Dentaku:

    resultNum = 0

    def __init__(self):
        self.resultNum = 0


    def input(self, inputStr :str) -> int:
        inputArray = inputStr.split(" ")
        for i in range(0, len(inputArray)):
            if inputArray[i] == "+":
                self.plus(int(inputArray[i+1]))
            if inputArray[i] == "-":
                self.minus(int(inputArray[i+1]))
            if inputArray[i] == "*":
                self.multiple(int(inputArray[i+1]))
            if inputArray[i] == "/":
                self.divison(int(inputArray[i+1]))
            if i == 0:
                self.plus(int(inputArray[0]))
        
        return self.getNum()

    def plus(self, inputNum :int):
        self.resultNum += inputNum

    def minus(self, inputNum: int):
        self.resultNum -= inputNum

    def multiple(self, inputNum :int):
        self.resultNum *= inputNum

    def divison(self, inputNum :int):
        self.resultNum /= inputNum

    def getNum(self) -> int:
        return self.resultNum