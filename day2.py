import numpy as np

input = open("day2input.txt", "r")

games = np.empty((100, 3))
switch = {
          'red': 0,
          'green': 1,
          'blue': 2
      }
limits = {
          0: 12,
          1: 13,
          2: 14
      }


for line in input:
   gameNum = int(line.split(':')[0].split(' ')[1])
   pulls = line.split(':')[1].split(';')
   maxRed = 0
   maxGreen = 0
   maxBlue = 0
   for i in range(len(pulls)):
      gameCounts = pulls[i].split(',')
      red = 0
      green = 0
      blue = 0
      for j in range(len(gameCounts)):
        color = switch.get(gameCounts[j].split(' ')[2].strip())
        count = int(gameCounts[j].split(' ')[1])
        if color == 0:
          red += count
        elif color == 1:
          green += count
        elif color == 2:
          blue += count
      if red > maxRed:
        maxRed = red
      if green > maxGreen:
        maxGreen = green
      if blue > maxBlue:
        maxBlue = blue
   games[gameNum-1][0] = maxRed
   games[gameNum-1][1] = maxGreen
   games[gameNum-1][2] = maxBlue

validSum = 0

for i in range(100):
  valid = True
  for j in range(3):
    if games[i][j] > limits.get(j):
      valid = False
  if valid:
    validSum += i+1

print(validSum)


