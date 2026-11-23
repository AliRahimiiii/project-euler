# def howManyTens(remainder, d):
#     k = 1
#     while 10**k*remainder < d:
#         k+=1
#     return k 

# def divider(d):
#     dividendsSeen = []
#     result = ""
#     newRemainder = 1
#     count = 1
#     while count <= 1000:
#         k = howManyTens(newRemainder, d)
#         dividend = 10**k * newRemainder
#         newRemainder = dividend % d
#         result = result + (k-1)*"0"
#         result = result + str(int(dividend / d))
#         count += 1
#         if newRemainder == 0:
#             break
#     return result

# def cycleFinder(result:str):
#     if len(result) == 1:
#         return result
#     index = 1
#     char = result[index-1]
#     rest = result[index:]
#     if char not in  rest:
#         return cycleFinder(rest)
#     else:
#         firstCharInTheRest = rest.index(char)
#         candidate = result[index-1:index+firstCharInTheRest]
#         return candidate

# print(divider(31*37))
# print(cycleFinder(divider(31*31)))


def cycle_len(d):
    while d % 2 == 0: d //= 2
    while d % 5 == 0: d //= 5
    if d == 1:
        return 0            # terminating decimal
    r, k = 10 % d, 1
    while r != 1:           # remainder returns to 1
        r = r * 10 % d
        k += 1
    return k

best_len = 0
best_d = 0
for d in range(999, 1, -1):
    if d - 1 < best_len:
        break
    current = cycle_len(d)
    if best_len < current:
        best_len, best_d = current, d

print(best_d)