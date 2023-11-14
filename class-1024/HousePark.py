class HousePark:
    lastname = "박"

    def __init__(self, name):
        self.fullname = self.lastname + name

    def set_name(self, name):
        self.fullname = self.lastname + name

    def travel(self, where):
        print("%s, %s여행을 가다." % (self.fullname, where))


print(__name__)

if __name__ == '__main__':
    pey = HousePark("응용")
    # pey.set_name()
    print(pey.fullname)
    pey.travel('부산')
