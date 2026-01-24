def add(*args):
    sum = 0
    for each_num in args:
        sum += each_num

    return sum


print((add(3, 4, 5)))