""""# count how many times each fruit appears
fruits = ["apple", "kiwi", "apple", "fig", "kiwi", "apple"]
counts = {}

for fruit in fruits:
    if fruit not in counts:
        counts[fruit] = 1
    else:
        counts[fruit] += 1

for fruit in counts:
    print(fruit, counts[fruit])"""""





fruits = ["apple", "kiwi", "apple", "fig", "kiwi", "apple"]
counts = {}

for fruit in fruits:
    if fruit not in counts:
        counts[fruit] = 1
    else:
        counts[fruit] += 1

for fruit in counts:
    print(fruit, counts[fruit])















