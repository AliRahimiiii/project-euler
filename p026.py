def howManyTens(remainder, d):
    k = 1
    while 10**k*remainder < d:
        k+=1
    return k 

def divider(d):
    dividendsSeen = []
    result = ""
    newRemainder = 1
    count = 1
    while count <= 1000:
        k = howManyTens(newRemainder, d)
        dividend = 10**k * newRemainder
        newRemainder = dividend % d
        result = result + (k-1)*"0"
        result = result + str(int(dividend / d))
        count += 1
        if newRemainder == 0:
            break
    return result

def cycleFinder(result:str):
    if len(result) == 1:
        return result
    index = 1
    char = result[index-1]
    rest = result[index:]
    if char not in  rest:
        return cycleFinder(rest)
    else:
        firstCharInTheRest = rest.index(char)
        candidate = result[index-1:index+firstCharInTheRest]
        return candidate

print(divider(31*37))
print(cycleFinder(divider(31*31)))
