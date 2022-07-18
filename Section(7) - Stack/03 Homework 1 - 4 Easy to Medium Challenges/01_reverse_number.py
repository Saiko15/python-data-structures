def reverse_num(num):
    if num == 0:
        return 0

    stk = []
    while num:
        stk.append(num % 10)
        num //= 10

    tens = 1
    while stk:
        num = stk[-1] * tens + num
        tens *= 10
        stk.pop()

    return num


print(reverse_num(123450000))   # 54321