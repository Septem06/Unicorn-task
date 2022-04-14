import random


STARTING_BALANCE = 100
balance = STARTING_BALANCE


for item in range(10):
    number =random.randint(1,100)

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

    print(f"token: {token}, balance: ${balance:.2f}")

print()
print(f"Starting balance = ${STARTING_BALANCE:.2f}")
print(f"final balance = ${balance:.2f}")
