"""
Consider: (()(()))
We know any valid sub-expression can be replaced with its value. Let's find smallest ones

( () ( () )) ==> ( 1+ ( () )) ==> ( 1 ( 1 )) ==> (1 + 2) ==> (3) ==> 6
We see that subexpressions () with value 1 and (()) with value 2 are part of a bigger expression (()(()))

We can write inefficient code to keep find internal small expressions, but can we do smarter?

Thinking in processing left to right: we either
- have ( to indicate a new subexpression that will have ) in future
- or ) to indicate there is a subexpression that is done now

Stack can help us to do that
- We find (, we add 0: it represents the initial sum of the internal subexpressions
- We find ), we finish a subexpression value and accumulate to its parent

It might not be easy to get idea, but its solution can be a similar thinking style in other stack problems

"""
class Solution:
    def scoreOfParentheses(self, exp):
        stk = [0]   # temp value to help us

        for char in exp:
            if char == '(':
                stk.append(0)   # new parent: current sum = 0
            else:
                # An expression will be closed
                # Find its value: either 1 for empty () or 2 * its sub-expressions
                # we can calc both with a simple max()
                value = max(2 * stk.pop(), 1)

                # Add the expression sum to its parent current sum
                #  Assume we have expression E that is (CHD)
                # where C, H, D are valid-subexpressions with values 5, 10, 4
                # then E is (5+10+4) = (19) = 38
                # Every time we finish an expression, we add its value to its parent
                # get the parent and update its sum with a finished sub-expression
                stk[-1] += value

        return stk.pop()


if __name__ == '__main__':
    sol = Solution()
    print(sol.scoreOfParentheses('(()())'))
