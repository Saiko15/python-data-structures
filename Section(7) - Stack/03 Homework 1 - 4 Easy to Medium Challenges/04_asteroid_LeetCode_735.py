# https://leetcode.com/problems/asteroid-collision/solution/
 
class Solution(object):
    def asteroidCollision(self, asteroids):
        results = []
        
        for ast in asteroids:
            # For every new asteroid, remove all what will explode
            # Only may happens when asteroid going backword and something coming forward
            #       asteroid < 0 < stack.peek()
            while results and ast < 0 < results[-1]:
                if results[-1] < -ast:      # last will explode.
                    results.pop()
                    continue
                elif results[-1] == -ast:   #  both exploded
                    results.pop()
                break
            else:
                results.append(ast)
        return results

if __name__ == '__main__':
    sol = Solution()
    print(sol.asteroidCollision([10,2,-5]))