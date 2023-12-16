import re

input = open("day1input.txt", "r")
sum = 0
for line in input:
    numbers = re.findall(r'\d', line)
    thisNum = numbers[0]+numbers[-1]
    sum += int(thisNum)
print(sum)

