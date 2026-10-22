import math

def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result


numerator = math.prod([i for i in range(21,41)])
denominator = math.prod([i for i in range(1,21)])

print(int(numerator/denominator))