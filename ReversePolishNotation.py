def evaluate(expression):
    expression = expression.split() # splitting expression at whitespaces

    stack = []

    for ele in expression:
        if ele not in '/*+-':
            stack.append(int(ele))

        # getting operands
        else:
            right = stack.pop()
            left = stack.pop()

        # performing operation according to operator
        if ele == '+':
            stack.append(left + right)

        elif ele == '-':
            stack.append(left - right)

        elif ele == '*':
            stack.append(left * right)

        elif ele == '/':
            stack.append(int(left / right))

    return stack.pop()

arr = "10 6 9 3 + -11 * / * 17 + 5 +"

answer = evaluate(arr)
print(f"Value of given expression'{arr}' is {answer}")






