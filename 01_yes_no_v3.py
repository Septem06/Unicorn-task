show_instructions = input("have you played this game before? :").lower()
if show_instructions == "yes" or show_instructions == "y":
    print("program continues")
elif show_instructions == "no" or show_instructions == "n":
    print("display instructions")
else:
    print("please answer 'yes' or 'no' ")
print(f"you entered'{show_instructions}'")
