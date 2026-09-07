import random
expected_number = random.randint(1, 10)
attempt = 0
trial = 3
while attempt < trial:
    try:
        guess = int(input("Enter your guess number: "))
        attempt += 1
        if guess == expected_number:
            print("congratulation, you guess right")
            break
        if attempt < trial:
            print(f"{attempt} left")
        else:
            print(f"you have run out of trial")
    except (ValueError, NameError):
        print("Not a valid number")

