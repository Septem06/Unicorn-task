import random

tokens = ["unicorn", "horse", "donkey", "zebra"]
balance = 100

for item in range(20):
    token = random.choice(tokens)
    print(token, end='\n')

    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= 1
    else:
        balance -= .50

    print(f"token: {token}, balance: ${balance}")
