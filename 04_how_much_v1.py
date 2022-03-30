user_balance = int(input("how much do u want to play with (must be a number between 1 and 10) $"))

while not 1 <= user_balance <= 10:
    print("try again. please enter a whole number between 1 and 10")
    user_balance = int(input("how much do u want to play with $"))

print(f"you are playing with ${user_balance}")
