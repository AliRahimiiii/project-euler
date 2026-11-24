import math

def isPrime(num):
    if num < 0:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True

primes = []
for n in range(2,1001):
    if isPrime(n): primes.append(n)

highest_n = 0
for prime in reversed(primes):
    for a in range(-1000,1000):
        n = 0
        while isPrime(n**2 + a * n + prime): n+=1
        if n - 1 > highest_n:
            highest_n = n - 1
            print(a * prime, highest_n)
