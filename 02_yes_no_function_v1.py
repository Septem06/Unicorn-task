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


show_instructions = yes_no("have you played this game before? ")
print(f"you entered'{show_instructions}'")
print()
having_fun = yes_no("Are you having fun? ")
print(f"you entered'{having_fun}'")
