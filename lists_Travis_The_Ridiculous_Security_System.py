# Example of using and manipulating data with Python lists

known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred"]

print(len(known_users))
print("There are {} registered users named {}".format(len(known_users), known_users))



while True:
	print("Hi, my name is Travis!")
	name = input("What is your name? ").strip().capitalize()
	
	if name in known_users:
		print("Hello {}!".format(name))
		remove = input("Would you like to be removed from the system (y/n)? ").strip().lower()
		if remove == "y":
			print(known_users)
			known_users.remove(name)
			print(known_users)
		elif remove == "n":
			print("No problem, take care.")
	else:
		print("Hmm, I don't believe we've met {}".format(name))
		add_me = input("Would you like to be added from the system (y/n)? ").strip().lower()
		if add_me == "y":
			print(known_users)
			known_users.append(name)
			print(known_users)
		elif add_me == "n":
			print("No problem, see you around")
