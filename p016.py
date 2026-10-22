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

    
def sum(input1, input2):
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

def bigMultiply2(input1):

    return sum(input1, input1)


def bigPower2(power):
    result = "1"
    while power >= 1:
        result = bigMultiply2(result)
        power -= 1
    return result

def sumOfDigits(number):
    total = "0"
    for digit in number:
        total = sum(total, digit)
    return total

print(sumOfDigits(bigPower2(1000)))