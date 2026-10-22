
def divisors(num):
    divis = {1, num}
    i = 2
    while i not in divis:

        if num % i == 0:
            divis.add(i)
            divis.add(int(num/i))


        i += 1

    return divis



n = 8
while len(divisors(n*(n+1)/2)) <= 500:
    n+=1

print(n*(n+1)/2)