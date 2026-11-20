# 1 print each letter
# 2 make a counter, check each letter
# 3 print the count
word = 'hello'

count = 0

for letter in word:
    print(letter)
    if letter == 'l':
        count += 1
print(f"the letter l = {count}")