class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        result = self.first + self.second
        print("%d + %d = %d" % (self.first, self.second, result))
        return result

    def mul(self):
        result = self.first * self.second
        print("%d * %d = %d" % (self.first, self.second, result))
        return result

    def sub(self):
        result = self.first - self.second
        print("%d - %d = %d" % (self.first, self.second, result))
        return result

    def div(self):
        result = self.first / self.second
        print("%d / %d = %f" % (self.first, self.second, result))
        return result

    def floorDiv(self):
        result = self.first // self.second
        print("%d // %d = %f" % (self.first, self.second, result))
        return result


a = FourCal()
b = FourCal()

a.setdata(4, 2)
b.setdata(7, 3)

a.sum()
a.mul()
a.sub()
a.div()
a.floorDiv()

b.sum()
b.mul()
b.sub()
b.div()
b.floorDiv()
