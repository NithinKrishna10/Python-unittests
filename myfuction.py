import math


def multiply_with_loop_imperfect(x,y):
    return sum(y for _ in range(x))

# print(myfuction(100))

def multiply_with_loop_better(x,y):
    if (x >=0 and y >= 0) or (x < 0 and y <0):
        return sum(abs(y) for _ in range(abs(x)))
    elif x<0:
        return sum(x for _ in range(y))
    else:
        return sum(y for _ in range(x))


def length_of_integer(n):
    return int(math.floor(math.log10(n))+1)



multiply_with_loop_imperfect(10,70)