class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'{self.data}'


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert_end(self, value):
        node = Node(value)
        self.length += 1

        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def delete_front(self):  # O(1) time - O(1) memory
        if not self.head:
            return

        value = self.head.data
        next = self.head.next
        self.length -= 1
        self.head = next

        if self.length <= 1:
            self.tail = self.head

        return value

    def __repr__(self):
        represent = ''
        temp_head = self.head

        while temp_head is not None:
            represent += str(temp_head.data)
            temp_head = temp_head.next
            if temp_head:
                represent += ', '

        return represent


class Queue:
    def __init__(self):
        self.lst = LinkedList()

    def enqueue(self, value):
        self.lst.insert_end(value)

    def dequeue(self):
        assert not self.empty()
        return self.lst.delete_front()

    def empty(self):
        return self.lst.length == 0

    # Enhanced Functionalities to use the queue
    def size(self):
        return self.lst.length

    def front(self):
        assert not self.empty()
        return self.lst.head.data

    def display(self):
        if self.empty():
            print("EMPTY\n")
        else:
            print(self.lst)


class PriorityQueue:
    def __init__(self):
        # Create 3 queues: one per priority
        self.q1 = Queue()
        self.q2 = Queue()
        self.q3 = Queue()

    def enqueue(self, value, priority):
        assert 1 <= priority <= 3

        if priority == 1:
            self.q1.enqueue(value)
        elif priority == 2:
            self.q2.enqueue(value)
        else:
            self.q3.enqueue(value)

    def dequeue(self):
        assert not self.empty()

        if not self.q3.empty():
            return self.q3.dequeue()

        if not self.q2.empty():
            return self.q2.dequeue()

        return self.q1.dequeue()

    def empty(self):
        return self.q1.empty() and self.q2.empty() and self.q3.empty()

    def display(self):
        if self.empty():
            print("EMPTY\n")
            return

        if not self.q3.empty():
            print('Priority #3 tasks', end=' ')
            self.q3.display()

        if not self.q2.empty():
            print('Priority #2 tasks', end=' ')
            self.q2.display()

        if not self.q1.empty():
            print('Priority #1 tasks', end=' ')
            self.q1.display()



if __name__ == '__main__':
    
    tasks = PriorityQueue()

    tasks.enqueue(1131, 1)
    tasks.enqueue(3111, 3)
    tasks.enqueue(2211, 2)
    tasks.enqueue(3161, 3)

    tasks.display()
    # Priority #3 tasks 3111, 3161
    # Priority #2 tasks 2211
    # Priority #1 tasks 1131

    print(tasks.dequeue())  # 3111
    print(tasks.dequeue())  # 3161

    tasks.enqueue(1535, 1)
    tasks.enqueue(2815, 2)
    tasks.enqueue(3845, 3)
    tasks.enqueue(3145, 3)

    tasks.display()
    # Priority #3 tasks 3845, 3145
    # Priority #2 tasks 2211, 2815
    # Priority #1 tasks 1131, 1535

    while not tasks.empty():
        print(tasks.dequeue(), end = ' ')
    # 3845 3145 2211 2815 1131 1535
