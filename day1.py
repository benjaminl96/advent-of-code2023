import re

input = open("day1input.txt", "r")
sum = 0
nums = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9
       }
for line in input:
    numbers = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
    print(numbers)
    firstNum = numbers[0]
    lastNum = numbers[-1]
    print(firstNum, lastNum)
    if firstNum in ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'):
        firstNum = nums.get(firstNum)
    if lastNum in ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'):
        lastNum = nums.get(lastNum)
    thisNum = str(firstNum)+str(lastNum)
    print(thisNum)
    sum += int(thisNum)
print(sum)

