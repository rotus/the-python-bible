#get user email address

email = input("What is your email address? ").strip()

#slide out user name, slice everything up to @

user = email[:email.index("@")]

#slide out domain name, slice everything after @, but +1 so not to include @ symbol

domain = email[email.index("@") + 1 :]

#format message

output = "Your username is {} and your domain name is {}".format(user,domain)

#display

print(output)


