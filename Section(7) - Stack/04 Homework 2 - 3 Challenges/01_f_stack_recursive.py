
def f(n):
    if n <= 1:
        return 5
    if n % 3 == 0:
        return 6 + f(n-1-n%3)
    return 8 + f(n-1-n%2)


def f_stk(n):
    if n <= 1:
        return 5
    
    class RecursiveCall:
        def __init__(self, n, result = 0, is_completed = False):
            self.n = n
            self.result = result
            self.is_completed = is_completed

    stk = [RecursiveCall(n)]

    while stk:
        n, result, is_completed = stk[-1].n, stk[-1].result, stk[-1].is_completed

        if not is_completed:     # a new recursive call
            if n <= 1:
                stk.append(RecursiveCall(n, 5, True))
            elif n % 3 == 0:
                stk.append(RecursiveCall(n-1-n%3, 6, False))
            else:
                stk.append(RecursiveCall(n-1-n%2, 8, False))
        else:
            stk.pop()

            if not stk:
                return result
            # Update parent caller
            stk[-1].result += result
            stk[-1].is_completed = True
            
    return None


if __name__ == '__main__':
    print(f(500), f_stk(500))   # 2503 2503

    #print(f(100000))     # maximum recursion depth exceeded in comparison
    print(f_stk(100000))  # 500007