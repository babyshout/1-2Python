# adder3.py
class Calculator:
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result


cal1 = Calculator()
cal2 = Calculator()

cal = Calculator

print("cal : ", cal)
print("cal1 : ", cal1)
print("cal2 : ", cal2)

print("cal() : ", cal())
print("cal() : ", cal())

print("cal().adder(20) : ", cal().adder(20))
print("cal().adder(20) : ", cal().adder(20))

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))
