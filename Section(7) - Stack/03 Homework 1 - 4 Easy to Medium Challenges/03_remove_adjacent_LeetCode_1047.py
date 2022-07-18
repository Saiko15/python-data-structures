# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, str):
        stk = []
        for char in str:
            if stk and char == stk[-1]:
                stk.pop()
            else:
                stk.append(char)

        return ''.join(stk)


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicates('abbaca'))   # ca
