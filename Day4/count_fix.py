words = ["cat", "dog", "cat", "cow", "dog", "cat"]
count = {}

for word in words:
    if word not in count:
        count[word] = 1
    else:
        count[word] +=1

print(count)
