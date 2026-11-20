animals = ["cat", "cow", "dog", "duck", "cat", "deer"]
count = {}

for animal in animals:
    if animal in count:
        count[animal] += 1
    else:
        count[animal] = 1
print(count)
counts ={}
for animal in animals:
    letter = animal[0]
    if letter not in count:
        counts[letter] = 1
    else:
        counts[letter] += 1
print(counts)