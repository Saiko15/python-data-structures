
def operation(a, b, oper):
    if oper == '+':
        return a + b
    if oper == '-':
        return a - b
    if oper == '*':
        return a * b
    if oper == '/':
        return a / b
    return a ** b	# ^


def evalaute_postfix(postfix):
    numbers = []	# stack of NUMBERS

    for char in postfix:
        if char.isdigit():
            numbers.append(float(char))
        else:
            a, b = numbers[-1], numbers[-2]
            numbers.pop()
            numbers.pop()
            # Careful: b, NOT a, consider 8/2 ==> 82/  a = 2, b = 8
            numbers.append(operation(b, a, char))

    return numbers[-1]

if __name__ == '__main__':
    assert evalaute_postfix('52/') == 2.5
    assert evalaute_postfix('12+3+') == 6
    assert evalaute_postfix('123*+') == 7
    assert evalaute_postfix('23*4+') == 10
    assert evalaute_postfix('135*+72/-') == 12.5
    assert evalaute_postfix('23452*-*93/6+*+') == -160
    assert evalaute_postfix('432^^') == 262144
    assert evalaute_postfix('5432^^+9-') == 262140





    # Tip: we shouldn't use == to compare float values
