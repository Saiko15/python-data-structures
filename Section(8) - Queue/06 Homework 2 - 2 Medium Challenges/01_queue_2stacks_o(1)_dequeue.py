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




class Queue:
    def __init__(self):
        self.stk1, self.stk2 = Stack(), Stack()

    @staticmethod
    def _move(stk1, stk2):
        """Move data from stack 1 to stack 2, hence reversed"""
        while not stk1.empty():
            stk2.push(stk1.pop())

    # Design: stack1 has all the data and its top matches queue front
    #         stack2 is just a temporary helper

    # assume we enqueue: [1, 2, 3, 4]
    # assume we built stack to be s1 = [4, 3, 2, 1 (top)] 
    #       That is: it matches queue output
    # let's enqueue 5
    # move s1 to s2: s2 = [1, 2, 3, 4]
    # push 5 to s1: s1 = [5]
    # move s2 to s1: [5, 4, 3, 2 ,1]
    # 2 moves: reverse and cancel it
    def enqueue(self, value):   # O(n)
        self._move(self.stk1, self.stk2)
        self.stk1.push(value)
        self._move(self.stk2, self.stk1)

    def dequeue(self):          # O(1)
        assert not self.empty()
        value = self.stk1.pop()
        return value

    def empty(self):
        return self.stk1.empty()



if __name__ == '__main__':
    qu = Queue()

    for i in range(1, 5):
        qu.enqueue(i)

    while not qu.empty():
        print(qu.dequeue(), end = ' ')
    # 1 2 3 4
