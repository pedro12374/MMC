import fractions


def lcm(a, b): return abs(a * b) / fractions.gcd(a, b) if a and b else 0

numbs = []

for i in range(1, 1001):
    numbs.append(i)

def MMC2(a,b):

    alfa = fractions.Fraction(a, b)
    MMC = alfa.denominator * a
    return MMC

def MMC3(a,b):
    alfa = fractions.Fraction(a,b)
    MMC = alfa.numerator * b
    return MMC
ok = []
no = []
for i in numbs:
    for j in numbs:
        x1 = i
        x2 = j
        MMCA = MMC2(x1,x2)
        MMCB = MMC3(x1, x2)
        MMCC = lcm(x1,x2)

        if MMCA == MMCB and MMCA == MMCC and MMCB == MMCC:
            ok.append('ok')
        else: no.append('no')

print len(ok)
print len(no)
