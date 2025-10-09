# Thomas Hatt
# Program 0.4v2
# Coms-170
# Current date: 10/8/2025

import random

# Initiate variables
currentRollSum = 0
totalRollCount = 0
totalOfAllRolls = 0

while currentRollSum != 12:
  # Roll dice
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)
  
  # Add dice together
  currentRollSum = dice1 + dice2
  
  # Increment roll count
  totalRollCount += 1
  
  # Add current roll to all rolls
  totalOfAllRolls += currentRollSum
  
  # Outputs
  print("\nCurrent roll #: " + str(totalRollCount))
  print("Dice 1: " + str(dice1))
  print("Dice 2: " + str(dice2))
  print("Sum of Dice 1 and Dice 2: " + str(currentRollSum))
  
# Calculate average roll
averageRoll = totalOfAllRolls / totalRollCount

# Final outputs
print("\n---------------")
print("Total rolls: " + str(totalRollCount))
print("Average of all rolls: " + str(round(averageRoll)))
print("---------------")