# For loop asking for user input 

vowels = 0
consonants = 0


word = input("Please give me a word: ")

for letter in word:
	if letter.lower() in "aeiou":
		vowels = vowels +1
	elif letter == " ":
		pass
	else:
		consonants = consonants +1

print("In the word {} there are {} vowels and {} consonants".format(word,vowels,consonants))

