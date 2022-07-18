def removeDuplicates(self, s: str) -> str:
    stk = []
    for char in s:
        if stk and char == stk[-1]:
            stk.pop()
            
        else:
            stk.append(char)

        
    return ''.join(stk)