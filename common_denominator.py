from functools import reduce
def common(a, b):
    denominators = [1]
    for i in range (2, a+1):
        while True:
            if a%i == 0 and b%i == 0:
                denominators.append(i)
                a /= i
                b /= i
            else:
                break
    den = reduce((lambda x, y: x * y), denominators)
    return den