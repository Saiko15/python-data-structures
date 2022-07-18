class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        assert self.items, 'No items!'
        return self.items.pop()

    def peek(self):
        assert self.items, 'No items!'
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Design: Let's force enqueue to be O(1)

# Assume we have enqueue: [(front) 1, 2, 3, 4 (last)]
# This way our stack 1 is: [1, 2, 3, 4 (top)]

# Now a deque has to get all the elements outside to get 1 (front)
# So let's move stack 1 to stack 2
# Stack2: [4, 3, 2, 1 (top)]
# pop = 1
# Assume more enqueue with [5, 6, 7]
# We can't just add them to stack 2. Let's put again in stack 1
# stack 1: [5, 6, 7 (top)]
# stack 2: [4, 3, 2 top)]
#
# data now scattered on 2 stacks! Can we merge? NO, data is corrupted!
# So?
# Keep using stack 1 for enqueue
# if we need to dequeue, then stack 2 elements are ready for us
# If stack 2 is empty, then just move stack 1 again!


class Queue:
    def __init__(self):
        self.stk1, self.stk2 = Stack(), Stack()

    @staticmethod
    def _move(stk1, stk2):
        """Move data from stack 1 to stack 2, hence reversed"""
        while not stk1.empty():
            stk2.push(stk1.pop())

    def enqueue(self, value):   # O(1)
        self.stk1.push(value)

    def dequeue(self):          # O(N)
        assert not self.empty()

        if self.stk2.empty():
            self._move(self.stk1, self.stk2)

        value = self.stk2.pop()
        return value

    def empty(self):
        return self.stk1.empty() and self.stk2.empty()



if __name__ == '__main__':


    qu = Queue()

    for i in range(1, 5):
        qu.enqueue(i)

    while not qu.empty():
        print(qu.dequeue(), end = ' ')
    # 1 2 3 4
