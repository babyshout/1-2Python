sum = lambda a, b: a + b
print(sum(3, 4))

myList = [
    lambda a, b: a + b,
    lambda a, b: a * b
]
print(myList)

print(myList[0])
print(myList[0](3, 4))

print(myList[1](3, 4))


def my_sum(a, b):
    return a + b


def my_mul(a, b):
    return a * b


myList1 = [my_sum, my_mul]

print(
    myList1[0](2, 4)
)
