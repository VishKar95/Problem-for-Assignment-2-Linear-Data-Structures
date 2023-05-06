def evaluate_postfix(expression):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])

    for char in expression:
        if char.isdigit():
            # if the character is a digit, push it onto the stack as an integer
            stack.append(int(char))
        elif char in operators:
            # if the character is an operator, pop two operands from the stack,
            # perform the corresponding operation, and push the result back onto the stack
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == '+':
                stack.append(operand1 + operand2)
            elif char == '-':
                stack.append(operand1 - operand2)
            elif char == '*':
                stack.append(operand1 * operand2)
            elif char == '/':
                stack.append(operand1 / operand2)
            elif char == '^':
                stack.append(operand1 ** operand2)

    # the final element on the stack is the result of the expression
    return stack[-1]
expression = '23*54*+9-'
print(evaluate_postfix(expression))  # output: 17
