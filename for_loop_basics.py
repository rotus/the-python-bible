# For loop basics

# Using ranges
for number in range(1,6):
	print(number)

# Using lists
for number in [5,6,7,8,9]:
	print(number)

for letter in "abcd":
	print(letter)

# Start/stop/step
for number in range(100,110,2):
	print(number)

# More complicated example

vowels = 0
consonants = 0

for letter in "America":
	if letter.lower() in "aeiou":
		vowels = vowels +1
	elif letter == " ":
		pass
	else:
		consonants = consonants +1

print("In the word America there are {} vowels and {} consonants".format(vowels,consonants))

