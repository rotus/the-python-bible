# Get random number generator
import random

# Define variables
health = 50
difficulty = 2 

# Display info
print("Health is {} and difficulty is {}".format(health, difficulty))

# Calc potion with random number and consider difficulty
potion_health = int(random.randint(25,50) / difficulty)
print("You find a potion with {} health".format(potion_health))

# Increase health with potion
health = health + potion_health
print("Your new health is {}".format(health))
