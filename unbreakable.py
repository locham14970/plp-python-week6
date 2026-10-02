<<<<<<< HEAD
def get_number():
    while True:
        try:
            number = int(input("Enter a whole number: "))
            return number
        except ValueError:
            print("Not a number. Please try again.")


number = get_number()
=======
def get_number():
    while True:
        try:
            number = int(input("Enter a whole number: "))
            return number
        except ValueError:
            print("Not a number. Please try again.")


number = get_number()
>>>>>>> e47bc319c39b07e831408815255a49fa12e118c2
print("You entered:", number)