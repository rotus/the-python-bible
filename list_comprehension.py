
even_numbers = [x for x in range(1,50) if x % 2 ==0]
print(even_numbers)


words = ["the","quick","brown","fox"]
# Print uppercase, losercase, length of each word
# Note this is a list inside a list
answer = [[w.upper(), w.lower(), len(w)] for w in words]
print(answer)
