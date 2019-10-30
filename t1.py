def mod(x, y):
    try:
        result = x % y
        return result
    # Cases of exception
    except ZeroDivisionError as zero:
        print("Incorrect input ,Can not Modolo by 0 ,try again")
        raise zero


def divide(x, y):
    try:
        result = x / y
        return result
    # Cases of exception
    except ZeroDivisionError as zero:
        print("Incorrect input ,Can not divide by 0 ,try again")
        raise zero

# lambda expressions of arithmetical action
# All operators must be in the dictionary


operators = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "pow": lambda x, y: x ** y,
    "/": divide,
    "%": mod
}


def get_number_and_validate():
    while True:
        try:
            print("Enter the number")
            num = float(input())
            # Cases of exception
        except ValueError:
            print("You did not enter a number ,try again")
        else:
            return num


def get_user_operator_and_validate():
    while True:
        print(f"Insert the arithmetical action {list(operators.keys())}")
        act = input().lower()
        if act in operators.keys():
            return act
        else:
            print("You did not enter a arithmetical action ,try again")


while True:
    try:
        # Receives input from the user

        num1 = get_number_and_validate()

        action = get_user_operator_and_validate()

        num2 = get_number_and_validate()

        answer = operators[action](num1, num2)

        print(f"Your answer is: {answer}")

    except ZeroDivisionError:
        """
        In case the exception is divisible by 0.
        There is no need to do anything
        because it has been discriminated by the function
        """
        pass
    except ArithmeticError:  # general exception
        print("Something went wrong, try again")
    else:
        break
