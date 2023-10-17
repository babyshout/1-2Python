class FourCal:
    def setData(first, second):
        print(first, second)

    def setdata(self, first: int, second: int):
        self.first = first
        self.second = second

    def sum(self):
        print('%d + %d = %d' %(self.first, self.second, self.first + self.second))
        return self.first + self.second


str
a = FourCal()
print(type(a))
print(a)

a.setdata(4, 2)
# FourCal.setdata(a, 4, 2)
print('a.first', a.first)
print('a.second', a.second)

b = FourCal()
b.setdata(3, 7)
print('b.first : ', b.first)
print('b.second : ', b.second)

b.sum()
