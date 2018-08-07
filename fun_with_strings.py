# Fun with String methods

data = "Hello sir"
print("The data we are going to manipulate is: {}".format(data))

print("There are {} letter L's".format(data.count("l")))

# Or just simply print count of L's

print(data.count("l"))

# Force UPPERcase

print("Let's capitalize all the words: {} ".format(data.upper()))

# Or simple version

print(data.upper())

print(data.capitalize())

# Capitalize first letter of all words
print(data.title())

# Is alpha will report false because space isn't alpha
print(data.isalpha())

# Obviously false, not all digits
print(data.isdigit())

y = "000000this is my data00000000"

print(y)

# Removes spaces, useful for input validation when sanitizing input
print(y.strip())

print(y.lstrip("0"))
print(y.strip("0"))

