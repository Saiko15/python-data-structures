# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, str):
        dct = {')': '(', ']': '[', '}': '{'}
        stk = []
        
        for char in str:
            if char not in dct:     # open
                stk.append(char)
            # empty or NO match
            elif not stk or dct[char] != stk.pop():
                return False

        return not stk  # MUST be empty


if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid('()[]{}'))    # True
    print(sol.isValid('{()[]}'))    # True
    print(sol.isValid('{()[]{'))    # False
