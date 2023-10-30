import sys


class Service:
    secret = "영구는 배꼽이 두개다"

    def sum(self, a, b):
        print('self : ', self)
        result = a + b;
        print("%s + %s = %s 입니다." % (a, b, result))


pey = Service()
print(pey.secret)

pey.sum(1, 1)
print(sys.getrefcount(Service))
print(Service == Service)
