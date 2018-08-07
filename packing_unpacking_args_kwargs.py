# Packing is extremely useful when you don't know how many arguments will be passed to function


print(1,2,3,4,5)

numbers = [1,2,3,4,5]
print(numbers)

# Asterick says unpack list and pass invididual #'s to function
print(*numbers)


# Add function that can be passed any # of arguments

def add(*numbers):
	total = 0
	for number in numbers:
		total = total + number
	print(total)

add(1,2,3,4,5,6,7,8,9)



# 1 star = normal arguments, 2 stars = keyword arguments

dictionary = {"name": "Adam", "age":23, "likes": "Python"}

def about(name, age, likes):
	sentence = "Meet {}! They are {} and like {}".format(name, age, likes)
	print(sentence)

about(**dictionary)


