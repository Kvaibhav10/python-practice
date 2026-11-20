counts = {"e": 3, "k": 1, "n": 2, "p": 2}

for key in counts:
    result =counts[key]
    if result >= 2:
        print(result)
        print(key, counts[key])