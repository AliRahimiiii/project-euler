
def advance(seq):
    tail = seq[-1]
    if tail == 1:
        return seq
    if tail % 2 == 0:
        seq.append(int(tail/2))
        return advance(seq)
    else:
        seq.append(3*tail+1)
        return advance(seq)


longest = 0
number = 1000_000
winner = 0
while number >= 13:
    number -= 1
    currentLength = len(advance([number]))
    if currentLength > longest:
        winner = number
    longest = max(longest, currentLength)
print(winner)