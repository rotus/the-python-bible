# Ask for name
name = input("What is your name?: ")

# Ask for age
age = int(input("What is your age?: "))

# Ask for city, strip santizes input and removes any errant spaces
city = input("Where do you live?: ").strip()

# Ask for what you enjoy
enjoy = input("What do you do for fun?: ")

# Create output text
string = "Your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name, age, city, enjoy)


# Print to screen
print(output)

