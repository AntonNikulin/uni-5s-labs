from Stack import Stack

OPERATORS = {
    #'operator': precedence of the operators
    '(': 1, 
    '+': 2,
    '-': 2,
    '*': 3,
    '/': 3,
}

NUMBERS = [str(i) for i in range(10)]

operatorsStack = Stack()
postfix = []

def infixToPostfix(infix):
    for el in infix.split():
        if el in NUMBERS:
            postfix.append(el)

        elif el == '(':
            operatorsStack.push(el)
            
        #from operatorsStack pop all operators until meeting left parenthesis
        elif el == ')':
            topOp = operatorsStack.pop()
            while topOp != '(':
                postfix.append(topOp)
                topOp = operatorsStack.pop()

        elif el in OPERATORS:
            while(not operatorsStack.isEmpty()) \
                      and (OPERATORS[operatorsStack.peek()] >= OPERATORS[el]):
                postfix.append(operatorsStack.pop())
            operatorsStack.push(el)

    while not operatorsStack.isEmpty():
        postfix.append(operatorsStack.pop())
    return postfix

input = raw_input("Infix: ")
print infixToPostfix(input)

#print operatorsStack.toList()
#print postfix


