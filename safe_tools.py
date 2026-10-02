<<<<<<< HEAD
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


def safe_number(text):
    try:
        return int(text)
    except ValueError:
        return "Not a number"


def get_field(learner, key):
    try:
        return learner[key]
    except KeyError:
        return "Field not found"


print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_number("42"))
print(safe_number("abc"))

learner = {"name": "Amina", "score": 82}
print(get_field(learner, "score"))
=======
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


def safe_number(text):
    try:
        return int(text)
    except ValueError:
        return "Not a number"


def get_field(learner, key):
    try:
        return learner[key]
    except KeyError:
        return "Field not found"


print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_number("42"))
print(safe_number("abc"))

learner = {"name": "Amina", "score": 82}
print(get_field(learner, "score"))
>>>>>>> e47bc319c39b07e831408815255a49fa12e118c2
print(get_field(learner, "email"))