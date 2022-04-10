import random

tokens = ["unicorn", "horse", "horse", "horse", "donkey", "donkey", "donkey", "zebra", "zebra", "zebra"]
STARTING_BALANCE = 100
balance = STARTING_BALANCE

for item in range(500):
    token = random.choice(tokens)

    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= 1
    else:
        balance -= .50

    print(f"token: {token}, balance: ${balance}")
    print(f"final balance = ${balance:.2f}")
