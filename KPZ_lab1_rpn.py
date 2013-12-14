import operator

OPERATORS = {
    '+':  operator.add,
    '-':  operator.sub,
    '*':  operator.mul,
    '/':  operator.div,
}

NUMBERS = [str(i) for i in range(10)]

input = raw_input("Infix: ")

stack = []
postfix = []

for el in input.split():
    if el in NUMBERS:
        postfix.append(el)

    elif el in OPERATORS:
        stack.append(el) #push

    elif el == ')':
        postfix.append(stack.pop())

print stack
print postfix
