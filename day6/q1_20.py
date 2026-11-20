marks = {"sam": 70, "alex": 85, "bob": 40}

for x in marks:
    print(x)

for x in marks.values():
    print(x)

for name, mark in marks.items():
    if mark >= 50:
        print(name, "pass")