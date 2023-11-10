n = 1
# while n < 1000:
#     print (n)
#     n +=1
#
# for n in range(1, 1000):
#     print(n)

for n in range(1, 1000):
    result = 0
    if n % 3 == 0 or n % 5 == 0:
        result += n
        print(n)
    print("result : ", result)
