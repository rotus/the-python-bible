# Create student dictionary

students = {
	"male":["Tom", "Charlie", "Harry", "Frank"],
	"female":["Sarah", "Emily", "Samantha"]
}

# Print out dictionary keys

for key in students.keys():
	print("Key: {} ".format(key))
		

# For each student, print name if contains letter A

for key in students.keys():
	for name in students[key]:
		if "a" in name:
			print(name) 
