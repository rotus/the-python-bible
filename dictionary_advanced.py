# Dictionary example using lists inside dictionary

print("-+"*50)

students1 ={
	"Alice":["ID001", 26, "A"],
	"Bob":["ID002", 21, "B"],
	"Claire":["ID003", 28, "C"],
	"Dan":["ID004", 18, "D"],
	"Emma":["ID005", 25, "E"]
	}

#

print(students1["Dan"])
print(students1["Dan"][0])

# Dictionary example using dictionaries INSIDE a dictionary
print("-+"*50)

students2 = {
	"Alice":{"id": "ID001", "age": 26, "grade":"A"},
	"Bob":{"id": "ID002", "age": 19, "grade":"B"},
	"Claire":{"id": "ID003", "age": 29, "grade":"C"},
	"Dan":{"id": "ID004", "age": 25, "grade":"D"},
	"Emma":{"id": "ID005", "age": 22, "grade":"F"},
	}

print(students2)

print(students2["Dan"]["age"])
print(students2["Emma"]["id"])
# print("Emmas grade {} ".format(len(students2))
print("Emma's Grade: {}".format(students2["Emma"]["grade"]))
