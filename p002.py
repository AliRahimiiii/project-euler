

pre = 1
num = 2
sum = 0

while num <= 4000_000:
    if num%2 == 0:
        sum += num

    hold = num
    num = num + pre
    pre = hold

print(sum)