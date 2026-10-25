def digitSum(char1, char2, carry):
    digit = int(char1) + int(char2) + carry
    return (int((digit - digit%10)/10), str(digit%10))

def zeroPadding(input1, input2):
    diff = len(input2) - len(input1)
    if diff > 0:
        input1 = input1[::-1] + diff*"0"
        return(input1[::-1], input2)
    elif diff < 0:
        input2 = input2[::-1] + abs(diff)*"0"
        return(input1, input2[::-1])
    else:
        return(input1, input2)

    
def bigSum(input1, input2):
    input1, input2 = zeroPadding(input1, input2)
    result = ""
    carry = 0
    digit = 0
    for i in reversed(range(len(input1))):
        carry, digit = digitSum(input1[i], input2[i], carry)
        result += digit
    if carry != 0:
        result += str(carry)
    return(result[::-1])



class fibonacci:
    def __init__(self):
        self.f1 = '1'
        self.f2 = '1'
        self.f3 = bigSum(self.f1, self.f2)
        self.i = 3
    def advance(self):
        self.i += 1
        self.f1 = self.f2
        self.f2 = self.f3
        self.f3 = bigSum(self.f1, self.f2)
    def report(self):
        return (self.f3, self.i)


seq = fibonacci()

while len(seq.report()[0]) < 1000:
    seq.advance()

print(seq.report()[1])
