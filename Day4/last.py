words = ["apple", "banana", "avocado", "blueberry", "cherry"]
result = {}

for word in words :
    letter = word[-1]
    if letter not in result:
        result[letter] = word

print(result)