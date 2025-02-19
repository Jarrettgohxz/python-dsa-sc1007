# x = a + b c%d >> e

class Stack:
    def __init__(self):
        self.data = None


operator_precedence = ['%', '+', '>>', '=']


def infix_to_postfix(infix: str):
    stack = Stack()

    postfix = ''

    for v in infix:
        if v == ' ':
            continue

        # current character is an operator
        if v in operator_precedence:
            while not stack.is_empty():
                operator_top_of_stack = stack.peek()

                # check operator at top of stack has equal or higher precedence than the current operator
                if operator_precedence.index(operator_top_of_stack) <= operator_precedence.index(v):
                    # pop operator from stack, append to postfix output
                    stack.pop()

                    postfix += operator_top_of_stack

        # current value is not an operator - an operand
        # elif v in ('x', 'a', 'b', 'c', 'd', 'e'):
        else:
            # simply add to postfix
            postfix += v

    #
    # after scanning through entire infix characters - pop remaining chars from stack and append to output postfix expression
    #
    while not stack.is_empty():
        postfix += (stack.pop())
