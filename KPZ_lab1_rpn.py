from Stack import Stack

OPERATORS = {
    '(': 1, #precedence of the operators
    '+': 2,
    '-': 2,
    '*': 3,
    '/': 3,
}

NUMBERS = [str(i) for i in range(10)]

input = raw_input("Infix: ")

operatorsStack = Stack()
postfix = Stack()

for el in input.split():
    if el in NUMBERS:
        postfix.push(el)

    elif el in OPERATORS:
        operatorsStack.push(el) 

    elif el == ')':
        postfix.push(operatorsStack.pop())

print operatorsStack.toList()
print postfix.toList()


