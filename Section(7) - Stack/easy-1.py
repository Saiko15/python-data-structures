# ○ 1234 ⇒ 4321
# ○ 123450000 ⇒ 54321 [drop trailing zeros]
def reverse_num(num): # 1234
    stk = [] # 4, 3, 2, 1
    while num:
        last_digit = num % 10 # 4 3 2 1 
        num = num // 10 # 123  12  1  0
        if last_digit:
            stk.append(last_digit) # 4 3 2 1
    res = 0
    mult = 1
    while stk:
        popo = stk.pop()
        res += (popo * mult) # 1 21 321 4321 
        mult *= 10
        
    return res


print(reverse_num(1234))
print(reverse_num(123450000))


