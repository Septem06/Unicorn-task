def num_check(question, low, high):
    error = "that was not valid input\n" "please enter a number between {} and {}\n" .format(low, high)

    while True:
        try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


user_balance = num_check("how much money would you like to play with? $", 1, 10)
print(f"you are playing with ${user_balance}")
