digits = {1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", 7 : "seven", 8 : "eight", 9 : "nine"}
tees = {20 : "twenty", 30 : "thirty", 40 : "forty", 50 : "fifty", 60 : "sixty", 70 : "seventy", 80 : "eighty", 90 : "ninety"}
doubleDigits = {10 : "ten", 11 : "eleven", 12 : "twelve", 13 : "thirteen", 14 : "fourteen", 15 : "fifteen", 16 : "sixteen", 17 : "seventeen", 18 : "eighteen", 19 : "nineteen"}

def numberToWord(number):
    ones = number % 10
    tens = int((number % 100 - ones)/10)
    hundreds = int((number - (tens + ones))/100)
    if number % 100 == number % 10 and number % 10 == number:
        return digits[number]
    elif number % 100 == number:
        if  tens == 1:
            return doubleDigits[number]
        elif ones != 0:
            return tees[tens*10] + digits[ones]
        else:
            return tees[tens*10]
    elif number % 100 != 0:
        return digits[hundreds] + "hundredand" + numberToWord(number % 100)
    else:
        return digits[hundreds] + "hundred"
    

print(len("onethousand")+sum([len(numberToWord(i)) for i in range(1, 1000)]))