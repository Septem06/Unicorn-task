import random

TEST_AMOUNT = 5
balance = TEST_AMOUNT

rounds_played = 0
play_again = ""

while play_again != "x":
    rounds_played += 1
    number = random.randint(1, 100)

    if 1 <= number <= 5:
        token = "unicorn"
        balance += 4

    elif 6 <= number <= 36:
        token = "donkey"
        balance -= 1

    else:
        if number % 2 == 0:
            token = "zebra"
            balance -= 0.5

        else:
            token = "horse"
            balance -= .5

    print(f"round {rounds_played}. token: {token}, balance: ${balance:.2f}")
    if balance < 1:
        print("\nsorry but you have run out of money")
        play_again = "x"
    else:
        play_again = input("\ndo you want to play another round?\n<enter> to play again or 'x' to exit ").lower()
    print()
print("thanks for playing")
print(f"you started with ${TEST_AMOUNT:.2f}")
print(f"and leave with ${balance:.2f}")
print("goodbye")
