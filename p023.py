from itertools import permutations

perm = permutations(range(10))


n=1
for i in perm:
    if n == 1e6: 
        print(i)
    n += 1