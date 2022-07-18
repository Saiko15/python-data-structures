
# Simple extension
# 1- Add prev(index) function
# 2- To remove from rear, first move to previous then get it
# 3- To enqueue_rear at the front, first move to previous then use it


class Deque:
    def __init__(self, size):
        self.added_elements = 0
        self.rear = self.front = 0
        # Let's use list to express our FIXED array
        self.array = [None] * max(1, size)

    def _next(self, pos):
        pos += 1
        if pos == len(self.array):
            pos = 0
        return pos
        # return (pos + 1) % size	#  Or shorter way

    def _prev(self, pos):
        pos -= 1
        if pos == -1:
            pos = len(self.array) - 1
        return pos
        # return (pos  - 1 + size) % size	#  Or shorter way

    def enqueue_rear(self, value):                   # old one
        assert not self.full()
        self.array[self.rear] = value
        self.rear = self._next(self.rear)
        self.added_elements += 1

    def enqueue_front(self, value):
        assert not self.full()
        self.front = self._prev(self.front)     # MOVE first
        self.array[self.front] = value
        self.added_elements += 1

    def dequeue_front(self):                    # old one
        assert not self.empty()
        value = self.array[self.front]
        self.front = self._next(self.front)
        self.added_elements -= 1
        return value

    def dequeue_rear(self):
        assert not self.empty()
        self.rear = self._prev(self.rear)      # MOVE first
        value = self.array[self.rear]
        self.added_elements -= 1
        return value

    def empty(self):
        return self.added_elements == 0

    def full(self):
        return self.added_elements == len(self.array)

    def display(self):
        print(f"Front {self.front} - rear {self.rear}", end = '\t')

        if self.full():
            print("FULL", end='')
        elif self.empty():
            print("EMPTY\n")
            return

        print("")
        cur = self.front

        for step in range(self.added_elements):
            print(self.array[cur], end=" ")
            cur = self._next(cur)
        print("")


if __name__ == '__main__':

    dq = Deque(6)
    dq.enqueue_front(3)
    dq.display()
    dq.enqueue_front(2)
    dq.enqueue_rear(4)
    dq.enqueue_front(1)
    dq.enqueue_front(5)
    dq.enqueue_front(6)

    dq.display() # 1 2 3 4
    print(dq.dequeue_rear())    # 4
    dq.display() # 1 2 3
    print(dq.dequeue_front())   # 1
    dq.display() # 2 3

    print(dq.dequeue_rear())    # 3
    print(dq.dequeue_front())   # 2

    while not dq.empty():
        dq.dequeue_rear()

    dq.display()
    for i in range(0, 6):
        dq.enqueue_rear(i + 10)
    dq.display()


'''
Front 5 - rear 0	
3 
Front 1 - rear 1	FULL
6 5 1 2 3 4 
4
Front 1 - rear 0	
6 5 1 2 3 
6
Front 2 - rear 0	
5 1 2 3 
3
5
Front 3 - rear 3	EMPTY

Front 3 - rear 3	FULL
10 11 12 13 14 15 
'''
