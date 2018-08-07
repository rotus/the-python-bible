# Randomly select a question, ask it until answered correctly

#import choice function from random, otherwise import random would work - but to call function you'd need to use random.choice()  ... this method is cleaner/easier
from random import choice

# Create a list of questions
q = [
	"Why is the sky blue? ", 
	"Why is there a face on the moon? ",
	"Why do you like pizza? "
	]

# Select a random question using choice function
question = choice(q)

answer = input(question).lower()

while answer != "just because":
	answer = input("why? :").strip().lower()

print("Oh.. Okay")
