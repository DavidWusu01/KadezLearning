import random

def guess_game():
    first_number = random.randint(0, 10)
    Attempt = 3 
    count = 0
    while count < Attempt:
        try:
            Guess_number = int(input("Enter guess number [0, 10]: "))
            count += 1
            if Guess_number == first_number:
                print(" congrats! you are correct.")
                break
            elif Guess_number > first_number:
                print("too high")
            elif Guess_number < first_number:
                print("too low") 
            else: 
                print("try again.")
        except ValueError:
            print("Enter a valid number")
    print(f"the guess number is {first_number}")        

def user_choice():
    while True:
        guess_game()
        print("Do you want to continue? ")
        print("1. yes")
        print("2. No")
        choice = int(input("Enter: "))
        if choice == 1:
            continue
        elif choice == 2:
            print("Thank you for trying")
            break
        else:
            print("Invalid")

user_choice() 