from kata import common_denominator
def proper_fractions(n):
    cgd = 0
    for i in range (1, n):
        if common_denominator.common(i, n) == 1:
            cgd+=1
    return cgd
