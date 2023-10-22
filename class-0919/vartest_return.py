# vartest_return.py

a = 1


def vartest(add):
    add = add + 1
    return add


a = vartest(a)
print(a)
