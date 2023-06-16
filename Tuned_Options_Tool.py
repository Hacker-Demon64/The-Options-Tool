Choice = int(input("Choose Your Option: "))

if Choice == 1:
    num1 = int(input("First Number: "))
    num2 = int(input("Second Number: "))
    result = num1 + num2
    print(result)

elif Choice == 2:
    Name = input("Please Input Your Name: ")
    print("Hi there, " + Name)
    Begin = input("Do You Want A Quiz?: ")
    if Begin.lower() == "yes":
        print("Alright, Let's Begin")
        questions = {
            "What Is 24 + 24?": "48",
            "What Is USB?": "Universal Serial Bus",
            "Which Programming Language Made YouTube?": "Python"
        }
        for question, answer in questions.items():
            user_answer = input(question + ": ")
            if user_answer.lower() == answer.lower():
                print("Wow Correct Answer")
            else:
                print("Oops! Wrong Answer")
                break
        else:
            print("Wow! You Have Won!")
    else:
        print("No problem!")

elif Choice == 3:
    import calendar
    year = 1994
    month = 2
    calendar_text = calendar.month(year, month)
    print(calendar_text)

elif Choice == 4:
    secret_word = "Elephant"
    guess = input("Guess The Word: ")
    if guess.lower() == secret_word.lower():
        print("You Won!")
    else:
        print("Better luck next time!")

else:
    print("Invalid Option")
