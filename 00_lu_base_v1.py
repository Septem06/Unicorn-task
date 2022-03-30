def yes_no(question_text):
    while True:
        answer = input(question_text).lower()
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer
        elif answer== "no" or answer == "n":
            answer = "No"
            return answer
        else:
            print("please answer 'yes' or 'no'")


def instructions():
    print(" How to Play *")
    print ()
    print ("The rules of the game will go here")
    print()




    played_before = yes_no("have you played this game before? ")

    if played_before == "no":
        instructions()



user_balance = num_check("how much money would you like to play with? $", 1, 10)
print(f"you are playing with ${user_balance}")
