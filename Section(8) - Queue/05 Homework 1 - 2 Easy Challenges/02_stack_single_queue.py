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

    def delete_front(self):                 # O(1) time - O(1) memory
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


class Stack:
    def __init__(self):
        self.queue = Queue()

    def push(self, item):	# O(N) based on linked-list impl
        # Design: keep the queue front always match stack top (e.g. ready to pop()
        # Hence, With every new element, we insert it at the FRONT

        # To insert at the front. Add the element, then circulate others around it
        sz = self.queue.size()
        self.queue.enqueue(item)
        
        for step in range(sz):
            self.queue.enqueue(self.queue.dequeue())

    def pop(self):	# O(1) based on linked-list impl
        return self.queue.dequeue()

    def peek(self):
        return self.queue.front()

    def empty(self):
        return self.queue.empty()

    # OOP Design tip: This class MUST NOT use the queue linked-list directly. Coupling is very bad
    # In other words, the queue's implementation may change in the future
    # BUT its ADT will remain the same. So we mainly use its ADT NOT its internals


if __name__ == '__main__':

    stk = Stack()
    stk.push(10)
    stk.push(20)
    stk.push(30)
    print(stk.peek())   # 30
    stk.push(40)
    print(stk.peek())   # 40

    while not stk.empty():
        print(stk.pop(), end=' ')
    # 40 30 20 10
