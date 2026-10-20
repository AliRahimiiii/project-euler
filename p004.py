
def isPalindrome(num):
    oneWay = str(num)
    theOther = oneWay[::-1]
    return int(oneWay) == int(theOther)




done = False
for i in range(999,899,-1):
    if done:
        break
    for j in range(999, 899, -1):
       num = i*j
       if isPalindrome(num):
            print(num)
            done = True
