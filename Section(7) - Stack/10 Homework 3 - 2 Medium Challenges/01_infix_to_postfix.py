def infixToPostfix(infix):
    operators = []
    postfix = ''

    def precedence(op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        if op == '^':
            return 3
        return 0

    infix += '-'		    # Whatever lowest priority: force stack got empty
    operators.append('#')   # Remove IsEmpty

    for char in infix:
        if char.isdigit() or char.islower() or char.isupper():
            postfix += char
        elif char == '(':
            operators.append(char)
        elif char == ')':
            while operators[-1] != '(':
                postfix += operators[-1]
                operators.pop()
            operators.pop() # pop (
        else:
            # Now we have to split > from ==
            # In case ==      The ^ is 'right to left' and shouldn't be pushed
            # Think 2^3^4: output is 23 and stack [^]: we popped it, output is 23^4^
            # But the correct output is 234^^ where 34^ is applied first!
            while precedence(operators[-1]) >  precedence(char) or \
                  precedence(operators[-1]) == precedence(char) and char != '^':
                postfix += operators[-1]
                operators.pop()
            operators.append(char)

    return postfix


if __name__ == '__main__':
    assert (infixToPostfix('1+2+3') == '12+3+')
    assert (infixToPostfix('1+2*3') == '123*+')
    assert (infixToPostfix('2*3+4') == '23*4+')
    assert (infixToPostfix('1+3*5-8/2') == '135*+82/-')
    assert (infixToPostfix('2+3*4-5*6+7') == '234*+56*-7+')

    assert (infixToPostfix('2+(3*4)') == '234*+')
    assert (infixToPostfix('2+(3*(4-5*2)*(9/3+6))') == '23452*-*93/6+*+')

    assert (infixToPostfix('4^3^2') == '432^^')
    assert (infixToPostfix('5+4^3^2-9') == '5432^^+9-')
    assert (infixToPostfix('a+B*2-c') == 'aB2*+c-')
    assert (infixToPostfix('a+b*(c^d-e)^(f+g*h)-i') == 'abcd^e-fgh*+^*+i-')

    assert (infixToPostfix('1+2^3^4*5-6') == '1234^^5*+6-')
    assert (infixToPostfix('(1+2)^3^(4*5-6)^2+1') == '12+345*6-2^^^1+')

