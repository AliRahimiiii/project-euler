import math

def isPrime(num):
    for i in range(2, 1 + int(math.sqrt(num))):
        if num % i == 0:
            return False

    return True

print(sum([i for i in range(2,2000_000) if isPrime(i)]))