"""
The general idea is close to infix to postfix
But consider first reversing the infix
Now code is very similar to postfix conversion
With only one change: LR/RL associativity of operators are reversed now
in our code style

Overall
    Reverse
    Modified Infix to postfix
    Reverse
"""

def InfixToPrefix(infix):
    def ReversedInfixToPostfix(infix):
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
                # For equality in normal postfix, /+- (LR) should popped but ^ (RL) shouldn't
                # But for reversed infix, then ^ is LR (popped) and /+- are (RL) don't pop
                while operators and (precedence(operators[-1]) > precedence(char) or
                      precedence(operators[-1]) == precedence(char) and char == '^'):
                    postfix += operators[-1]
                    operators.pop()
                operators.append(char)

        postfix += ''.join(reversed(operators))  # # remaining
        return postfix

    # reverse the string and swap ( with ) and the opposite
    # (1+2)^3-(4-5) ==> (5-4)-3^(2+1)
    reversed_infix = infix[::-1].replace('(', '$').replace(')', '(').replace('$', ')')
    reversed_postfix = ReversedInfixToPostfix(reversed_infix)
    return reversed_postfix[::-1]


if __name__ == '__main__':
    assert InfixToPrefix('1+2') == '+12'
    assert InfixToPrefix('9-2+3') == '+-923'
    assert InfixToPrefix('2*3+4') == '+*234'
    assert InfixToPrefix('4^3^2') == '^4^32'
    assert InfixToPrefix('1+2') == '+12'
    assert InfixToPrefix('1+2+3') == '++123'
    assert InfixToPrefix('2+4') == '+24'
    assert InfixToPrefix('1+3-8/2') == '-+13/82'
    assert InfixToPrefix('2+3-5+7') == '+-+2357'
    assert InfixToPrefix('2+(3*(4-5)*(9/3+6))') == '+2**3-45+/936'
    assert InfixToPrefix('5+4^3^2-9') == '-+5^4^329'
    assert InfixToPrefix('a+B-c') == '-+aBc'
    assert InfixToPrefix('a+(c^d-e)^(f+g*h)-i') == '-+a^-^cde+f*ghi'
    assert InfixToPrefix('1+2^3^4-6') == '-+1^2^346'
    assert InfixToPrefix('(1+2)^3^(4-6)^2+1') == '+^+12^3^-4621'
    assert InfixToPrefix('2^3^4^5^6') == '^2^3^4^56'
