from HousePark import HousePark
class HouseKim(HousePark):
    lastname = '김'
    def travel(self, where, day):
        print("%s, %s여행 %d일 가네." %(self.fullname, where, day))


print(__name__)

if __name__ == '__main__':
    juliet = HouseKim("줄리엣")
    juliet.travel('독도', 3)
