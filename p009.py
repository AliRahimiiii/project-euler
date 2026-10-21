#%%
import math

for k in range(1,501):
    delta = k**2/4 - 750*k + 250**2
    if delta >=0:
        a = 250 + k/2 - math.sqrt(k**2/4 - 750*k + 250**2)
        b = 250 + k/2 + math.sqrt(k**2/4 - 750*k + 250**2)
        c = 500 - k

        if a == int(a) and b == int(b) and c == int(c):
            print(f"a = {a}, b = {b}, c = {c}, {a**2 + b**2 == c**2}, product = {a*b*c}" )

# %%
