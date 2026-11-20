nums = [4, 7, 4, 2, 9, 7, 4]

count = {}

for num in nums:
    if num not in count:
        count[num] = 1
    else :
        count[num] += 1
print(count)


duplects = []
for counts in count :
    if count[counts] > 1:
        duplects.append(counts)
print(duplects)






















"""duplicates = []

for num in nums:
    if num not in duplicates :
        duplicates.append(num)

print(duplicates)
"""