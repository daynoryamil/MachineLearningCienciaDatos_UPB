import math

def f(x):
    return math.sqrt(x + 3) - x + 1

for x in range(0, 100):
    print("f({:.2f}) = {:.5f}".format(x, f(x)))
