def isValid(self, s: str) -> bool:
        brackets = {')' : '(',
                    '}' : '{',
                    ']' : '['}
        
        stk = []
        for brac in s:
            if brac not in brackets:
                stk.append(brac)
                
            elif not stk or brackets[brac] != stk.pop():
                return False
            
        return not stk