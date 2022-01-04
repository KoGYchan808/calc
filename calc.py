def Basic_calculator():
    num1 = int(input("choose a number: "))
    num2 = int(input("choose another number: "))
    add = num1 + num2
    subtract = num1 - num2
    multiply = num1 * num2
    divide = num1 / num2

    symbol = input("choose from 1, 2, 3, 4: ")
    if symbol == "1":
        return add
    elif symbol == "2":
        return subtract
    elif symbol == "3":
        return multiply
    elif symbol == "4":
        return divide
    else:
        return "ERROR!"

print(Basic_calculator())