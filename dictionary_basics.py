# Used to store values with "keys" and then can retreive values based on those keys

students = {"Alice":25, "Bob":27, "Claire":17, "Dan":21, "Emma":25}
print(students)

# extract Dan's value from dict

print(students["Dan"])

# Update Alice's age
print(students["Alice"])
students["Alice"] = 26
print(students["Alice"])

print(students.items())
print(students.keys())
print(students.values())
