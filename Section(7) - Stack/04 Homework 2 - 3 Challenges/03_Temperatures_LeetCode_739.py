# https://leetcode.com/problems/daily-temperatures/

"""
This is a common problem called: next greater number
It is used with other problems in complex setup

 Reverse thinking
    Instead of finding the next greater of an element
    Use an element to find all items it is greater than them

 We will add each new element in the stack waiting for its next greater

 Given a new number, iterate on all previous in the stack
    and mark my self as their next great
    but stop once found a number >= me
    why? because I can't be used for more numbers (he is better than me)

 O(n) time! We iterate on numbers ~twice

"""

"""
From editorial:

At first glance, it may look like the time complexity of this algorithm should be O(N^2)
 ), because there is a nested while loop inside the for loop. However, each element can only be added to the stack once, which means the stack is limited to N pops. Every iteration of the while loop uses 1 pop, which means the while loop will not iterate more than N times in total, across all iterations of the for loop.

An easier way to think about this is that in the worst case, every element will be pushed and popped once. This gives a time complexity of O(N).

Easier logic than what I said in the video
It is good to keep eye on how many elements in/out
"""
class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        answer = [0] *n
        stk = []

        for curr_day, curr_temp in enumerate(temperatures):
            # Pop until the current day's temperature is not
            # warmer than the temperature at the top of the stk
            while stk and temperatures[stk[-1]] < curr_temp:
                prev_day = stk.pop()
                answer[prev_day] = curr_day - prev_day
            stk.append(curr_day)

        return answer

if __name__ == '__main__':
    sol = Solution()
    print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))
