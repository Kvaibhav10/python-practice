while True:
    try:
        question = int(input("How many questions? "))
        if question > 10 or question < 1:
         print("Choose 1 to 10")
        else:
            print(f"OK, {question} questions")
            break

    except ValueError:
        print("Please type a number")