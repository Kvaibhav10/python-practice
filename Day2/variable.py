# 1 print each number
# 2 make a counter, check each even number
# 3 print the count

numbers = [4, 7, 10, 3, 8]
count = 0
for num in numbers:
    print(num)
    if num % 2 == 0:
        count +=1
print(f"total even number {count}")
