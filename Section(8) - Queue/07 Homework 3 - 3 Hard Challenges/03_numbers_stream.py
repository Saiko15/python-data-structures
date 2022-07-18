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

    def size(self):
        return self.lst.length

    def display(self):
        if self.empty():
            print("EMPTY\n")
        else:
            print(self.lst)


class LastKNumberSumStream:
    def __init__(self, k):
        self.k = k
        self.q = Queue()
        self.sum = 0


    def next(self, new_num):		# Compute and return sum of last K numbers sent so far
        self.q.enqueue(new_num)
        self.sum += new_num

        if self.q.size() > self.k:
            self.sum -= self.q.dequeue()

        return self.sum


if __name__ == '__main__':
    processor = LastKNumberSumStream(4)

    while True:
        num = int(input())
        print('Sum of last K numbers', processor.next(num))


'''
/home/moustafa/system-installs1/anaconda3/envs/pyt/bin/python /home/moustafa/workspaces/pycharm/temp/mainpy.py
1
Sum of last K numbers 1
2
Sum of last K numbers 3
3
Sum of last K numbers 6
4
Sum of last K numbers 10
5
Sum of last K numbers 14
6
Sum of last K numbers 18
7
Sum of last K numbers 22
8
Sum of last K numbers 26

'''