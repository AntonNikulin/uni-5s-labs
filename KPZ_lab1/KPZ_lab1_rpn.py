from Stack import Stack

OPERATORS = {
    #'operator': precedence of the operators
    '(': 1,
    '+': 2,
    '-': 2,
    '*': 3,
    '/': 3,
}

NUMBERS = [str(i) for i in range(100)]

operatorsStack = Stack()
postfix = []

def infixToPostfix(infix):
    for el in infix.split():
        if el in NUMBERS: #accept only numbers
            postfix.append(el)

        elif el == '(':
            operatorsStack.push(el)

            """from operatorsStack pop all operators until meet left parenthesis"""
        elif el == ')':
            topOp = operatorsStack.pop()
            while topOp != '(':
                postfix.append(topOp)
                topOp = operatorsStack.pop()

                """pop  all operators from stack that have
        equal or higher precedence, append them to postfix, and
        push the 'el' into the stack."""
        elif el in OPERATORS:
            while(not operatorsStack.isEmpty()) \
                      and (OPERATORS[operatorsStack.peek()] >= OPERATORS[el]):
                postfix.append(operatorsStack.pop())
            operatorsStack.push(el)

    """remaining
    operators from the stack to the postfix expression"""
    while not operatorsStack.isEmpty():
        postfix.append(operatorsStack.pop())
    return postfix

input = raw_input("Infix: ")
print infixToPostfix(input)

#print operatorsStack.toList()
#print postfix


