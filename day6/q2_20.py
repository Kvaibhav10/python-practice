#add the dict of name in maeks
#make 2 vaiable and use loops for marks
#use the if to check the marks accordig to this place the name
marks = {"sam": 90, "alex": 15, "bob": 100}
best_name = ''
best_marks = 0

for name,mark in marks.items():
    if mark > best_marks:
        best_marks = mark
        best_name = name

print(best_name,best_marks)