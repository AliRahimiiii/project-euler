import math

def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True

num = 600851475143
i = 2

while i <= num:
    if num%i == 0:
        factor = num/i
        if isPrime(factor):
            print(int(factor))
            break
    i += 1
    