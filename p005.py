#%%
import math

def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

#%%
primes = []

for i in range(2, 21):
    if isPrime(i):
        primes.append(i)

powers = []
for prime in primes:
    powers.append(int(math.log(20, prime)))

# %%
factors = list(primes[i]**powers[i] for i in range(len(primes)))
num = 1
for factor in factors:
    num *= factor
print(num)
# %%
