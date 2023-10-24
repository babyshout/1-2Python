class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        result = self.first + self.second
        print("%d + %d = %d" % (self.first, self.second, result))
        return result





a = FourCal()
a.setdata(4, 2)
print(a.sum())
