"""words = ["tree", "book", "pen", "cake", "lamp", "sun", "rose", "cup"]
result = {}

for word in words:
    letter = word[-1]
    if letter not in result:
        result[letter] = [word]
    else:
        result[letter].append(word)
print(result)
"""
fruits = ["apple", "kiwi", "fig"]

for f in fruits:
    print(f, f[0], len(f))

print(fruits[0], len(fruits))