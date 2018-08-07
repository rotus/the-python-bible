# Example using loops, data structures, strings

# Pig latin = pig -> igPay

print(" ____  _         _          _   _ ")
print("|  _ \(_) __ _  | |    __ _| |_(_)_ __")  
print("| |_) | |/ _` | | |   / _` | __| | '_ \ ")
print("|  __/| | (_| | | |__| (_| | |_| | | | |")
print("|_|   |_|\__, | |_____\__,_|\__|_|_| |_|")
print("         |___/ ")
print("")

#get sentence from user

original = input("What would you like my to convert?: ").strip().lower()

print("Okay, I'll convert: '{}'".format(original))

#split sentence into words using string method

words = original.split()

# loop through words and convert them to pig latin
# if starts it vowel, just add "yay"
# if starts with consonant cluster, move to end and add "ay"

new_words = []

for word in words:
	if word[0] in "aeiou":
		new_word = word + "yay"
		new_words.append(new_word)
	else:
		vowel_pos = 0
		for letter in word:
			if letter not in "aeiou":
				vowel_pos = vowel_pos + 1
			else:
				break
		cons = word[:vowel_pos]
		the_rest = word[vowel_pos:]
		new_word = the_rest + cons + "ay"
		new_words.append(new_word)

#stick words back together, using join string method

output = " ".join(new_words)

#output final result

print(output)
