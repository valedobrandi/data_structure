from stack import Stack

expresion = "5 10 + 30 5 / -"


def solve_expression(expre):
    stack = Stack()
    token_list = expre.split(" ")
    for token in token_list:
        if token == "+":
            result = stack.pop() + stack.pop()
            stack.push(result)
        elif token == "-":
            result = stack.pop() - stack.pop()
            stack.push(result)
        elif token == "/":
            result = stack.pop() / stack.pop()
            stack.push(result)
        elif token == "*":
            result = stack.pop() * stack.pop()
            stack.push(result)
        else:
            stack.push(int(token))
    return round(stack.peek(), 0)


def solve_string(expre):
    first = Stack()
    second = Stack()
    index_letter = 0

    for index, token in enumerate(expre):
        index_letter = index + 1
        if token == "(":
            break
        first.push(token)

    for index, token in enumerate(expre[index_letter:-1]):
        second.push(token)

    while not second.is_empty():
        letter = second.pop()
        first.push(letter)

    while not first.is_empty():
        letter = first.pop()
        second.push(letter)
    string = ""

    while not second.is_empty():
        letter = second.pop()
        string += letter

    return string


print(solve_string("a(bcdefghijkl(mno)p)q"))
