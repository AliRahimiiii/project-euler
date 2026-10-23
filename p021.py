
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

thaNums = set()

for i in range(3, 10_000):
    if i not in thaNums:
        di = sum(divisors(i) - {i})
        if sum(divisors(di) - {di}) == i and i != di:
            thaNums.add(i)
            thaNums.add(di)

print(sum(thaNums))