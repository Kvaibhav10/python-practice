#make the result vaiable as dict
# loops the names and check the lenght of name using len()
#use if and check the condution and prin the result
names = ["sam", "alex", "bob", "john", "eve", "mike"]


result = {}

for name in names:
    letter = len(name)
    if letter not in result:
        result[letter] = [name]
    else:
        result[letter].append(name)
print(result)