words = ["apple", "banana", "avocado", "blueberry", "cherry"]
result = {}

for i in words:
    letter = i[0]
    if letter not in result:
     result[letter] = [i]
    else:
        result.append(result[letter])
print(result)


