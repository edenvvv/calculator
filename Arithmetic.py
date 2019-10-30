"""
The function adds two numbers
"""


def add(num1, num2):
    result = num1 + num2
    return result


"""
The function subtracts two numbers
"""


def sub(num1, num2):
    result = num1 - num2
    return result


"""
The function multiplies two numbers
"""


def mul(num1, num2):
    result = num1 * num2
    return result


"""
The function divides two numbers
"""


def div(num1, num2):
    try:
        result = num1 / num2
        return result
        # Cases of exception
    except ZeroDivisionError as zero:
        print("Incorrect input ,Can not divide by 0 ,try again")
        raise zero
