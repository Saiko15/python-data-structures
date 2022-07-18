def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    stk = []
    for ast in asteroids:
        while stk and ast < 0 < stk[-1]:
            if stk[-1] < -ast:      # last will explode.
                stk.pop()
                continue
            elif stk[-1] == -ast:   #  both exploded
                stk.pop()
            break
        else:
            stk.append(ast)
                    
    return stk