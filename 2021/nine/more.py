import sys
import datetime as dt


def main(lines):
    locker_num = lines[0]
    queries = lines[1:]
    print(locker_num)
    shower = Shower()
    locker = Locker()
    locker.setLocker(locker_num)
    order = Order()
    for q in queries:
        checkQuery(q, shower, locker)


class Shower():
    stack = {"userID": "day"}

    def checkQuery(self, dateStr, userID, day):
        if not self.isOpen(dateStr):
            return False
        return self.isUserUsedThisDay(userID, day)

    def isOpen(self, dateStr):
        if isOpen(dateStr):
            return True
        print("shower: closed")
        return False

    def isUserUsedThisDay(self, userID, day):
        if userID in self.stack:
            if day == self.stack[userID]:
                print("shower: already accepted")
                return False
        return True

    def defineFee(self, age):
        if age < 12:
            return 700
        elif age >= 12 and age < 15:
            return 1000
        elif age >= 15 and age < 18:
            return 1200
        elif age >= 18:
            return 1500

    def UseShower(self, userID, age, day):
        self.stack[userID] = day
        fee = self.defineFee(int(age))
        print(f"shower: {userID} {fee}")


class Locker:
    stack = {"userID": 0}
    emptyCount = 0

    def setLocker(self, count):
        self.emptyCount = int(count)

    def checkQuery(self, dateStr, wantCount):
        if not self.isOpen(dateStr):
            return False
        return self.hasEmpty(wantCount)

    def isOpen(self, dateStr):
        if isOpen(dateStr):
            return True
        print("locker: closed")
        return False

    def hasEmpty(self, wantCount):
        if wantCount > self.emptyCount:
            print("locker: lack of lockers")
            return False
        return True

    def applyLocker(self, userID, dateStr, wantCount, dayStr):
        fee = self.defineFee(dateStr, dayStr, wantCount)
        if userID in self.stack:
            if self.stack[userID] - wantCount >= 0:
                self.stack[userID] = self.stack[userID] + wantCount
                if wantCount < 0:
                    fee = 0
            else:
                print("invalid number")
                return
        else:
            self.stack[userID] = wantCount
        self.emptyCount = self.emptyCount - int(wantCount)
        print(f"locker: {userID} {fee} {self.emptyCount}")

    def defineFee(self, dateStr, dayStr, wantCount):
        dateArray = dateStr.split(":")
        dayArray = dayStr.split("-")
        date = dt.date(int(dayArray[0]), int(dayArray[1]), int(dayArray[2]))
        if date.strftime("%a") in ["Sun", "Sat"]:
            if (9 <= int(dateArray[0]) and 16 >= int(dateArray[0])):
                return 700 * wantCount
            if (16 <= int(dateArray[0]) and 21 >= int(dateArray[0])):
                return 500 * wantCount
        else:
            if (9 <= int(dateArray[0]) and 16 >= int(dateArray[0])):
                return 500 * wantCount
            if (16 <= int(dateArray[0]) and 21 >= int(dateArray[0])):
                return 400 * wantCount

    def returnLocker(self, userID, returnCount):
        useCount = self.stack[userID]
        if useCount < returnCount:
            print("invalid number")
            return
        if useCount == self.stack[userID]:
            self.stack.pop(key[userID, None])
        else:
            print("locker: {userID} {fee} {self.emptycount}")


class Menu():
    def __init__(self, name, price, specialPrice, stock):
        self.name = name
        self.price = price
        self.specialPrice = specialPrice
        self.stock = stock


class Order():
    stack = []
    menustack = []

    def setLocker(self, count):
        self.emptyCount = count

    def isOpen(self, dateStr):
        if dataStr == "unOpen":
            print("order: closed")

    def checkOrder(self, orderMenu, count):
        if orderMenu in self.menu:
            print("order: no such menu item")
            return
        if self.menu[orderMenu] < count:
            print("order: sold out")

    def applyOrder(self, userID, orderMenu, count):
        self.stack.append(userID)
        self.menu[orderMenu] -= count
        print("order:  {userID} {fee} self.menu[orderMenu]")

    def checkmenuName(self, name):
        for menu in menustack:
            if menu.name == name:
                return False
        return True

    def addMenu(self, memuName, price, specialPrice, stock):
        if not checkmenuName(memuName):
            print("add: this menu item already exists")
            return
        menustack.append(Menu(memuName, price, specialPrice, stock))
        print("add: accepted")


def checkQuery(query, shower, locker):
    queryKind = query.split(":")[0]
    dayStr = query.split(" ")[1]
    dateStr = query.split(" ")[2]
    userID = query.split(" ")[3]
    if queryKind == "shower":
        age = query.split(" ")[4]
        if shower.checkQuery(dateStr, userID, dayStr):
            shower.UseShower(userID, age, dayStr)

    if queryKind == "locker":
        wantNum = int(query.split(" ")[4])
        if locker.checkQuery(dateStr, wantNum):
            locker.applyLocker(userID, dateStr, wantNum, dayStr)
    if queryKind == "lock":
        print("lock query")
    if queryKind == "order":
        print("order query")
    if queryKind == "add":
        print("add query")
    if queryKind == "change":
        print("change query")


def isOpen(dateStr):
    dateArray = dateStr.split(":")
    return (9 <= int(dateArray[0]) and 21 >= int(dateArray[0]))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
