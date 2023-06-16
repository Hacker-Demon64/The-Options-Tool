print("Hi There Guys This Is The Options Tool!")

print("You Have 3 Options Each Of Them Have Different Purposes!")

Option = input("Please Choose Your Option: ")
if Option == "1":
    num1 = input("Input Your First Number: ")
    num2 = input("Input Your Second Number: ")
    result = int(num1) + int(num2)
    print(result)
elif Option == "2":
    print("Welcome To The Quiz")
    print("Let's Begin The Questions")
    Q1 = input("What Is The Capital Of France?: ")
    if Q1 == "Paris":
        print("Correct Answer")
    else:
        print("Wrong Answer")
    Q2 = input("Who Painted The Mona Lisa?: ")
    if Q2 == "Leonardo Da Vinci":
        print("Wow Artist!")
    else:
        print("Wrong Again ")
    Q3 = input("What Is The National Fruit Of Japan?: ")
    if Q3 == "Cherry Blossom":
        print("Wow You Have WON!")
    else:
        print("Sorry You Lost!")
elif Option == "3":
    import calendar
    year = 2011
    month = 12 
    calendar_text = calendar.month(year,month)
    print(calendar_text)
else:
    print("Invalid Option")
