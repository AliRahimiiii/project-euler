
def divisors(num):
    if num == 1:
        return {1}
    divis = {1, num}
    i = 2
    while i not in divis:

        if num % i == 0:
            divis.add(i)
            divis.add(int(num/i))


        i += 1

    return divis

def isAbundant(num):
    return sum(divisors(num)-{num}) > num

def twoParts(n, abundants):
    for i in abundants:
        if i > 0 and n-i>0:
            yield (i, n-i)

goalNumbers = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23}
abundants = {12}
notAbundants = {1,2,3,4,5,6}
for n in range(25, 28124):
    out = False
    for x1, x2 in twoParts(n, abundants):
        if x1 not in abundants and x1 not in notAbundants:
            if isAbundant(x1) : abundants.add(x1)
            else: notAbundants.add(x1)
        if x2 not in abundants and x2 not in notAbundants:
            if isAbundant(x2) : abundants.add(x2)
            else: notAbundants.add(x2)
        if x2 in abundants and x1 in abundants:
            out = True
            break

    if not out:
        goalNumbers.add(n)

print(sum(goalNumbers))