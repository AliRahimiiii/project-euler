#%%
import math

def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

primes = [i for i in range(2,1000_000) if isPrime(i)]
#%%
print(primes[10_000])
# %%
