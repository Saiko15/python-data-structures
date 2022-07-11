import inspect


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'{self.data}'


class LinkedList:
    def __init__(self, initial_values=None):
        self.head = None
        self.tail = None
        self.length = 0

        self.debug_data = []  # add/remove nodes you use

        if initial_values:
            for value in initial_values:
                self.insert_end(value)

    def _add_node(self, node):
        self.debug_data.append(node)
        self.length += 1

    def _delete_node(self, node):
        if node in self.debug_data:
            self.debug_data.remove(node)
        else:
            print("Node does't exist!!")
            return

        self.length -= 1

    def debug_str_address(self):
        temp_head = self.head
        results = []

        while temp_head is not None:
            results.append(f'{temp_head.data}@{id(temp_head)}')
            temp_head = temp_head.next
        return results

    def debug_print_node(self, node):
        if node is None:
            print('None')
            return

        print(str(node.data).ljust(5), end=' -> ')
        next_value = 'None' if node.next is None else str(node.next.data)
        print(next_value.ljust(5), end='\t')

        if node == self.head:
            print("head")
        elif node == self.tail:
            print("tail")
        else:
            print("")

    def debug_print_existing_nodes(self, msg=None):
        if msg:
            print(msg)

        for node in self.debug_data:
            self.debug_print_node(node)

        print('*******************')

        self.debug_verify_data_integrity()

    def debug_verify_data_integrity(self):
        if self.length == 0:
            assert self.head is None
            assert self.tail is None
            return

        assert self.head is not None
        assert self.tail is not None
        assert self.tail.next is None

        if self.length == 1:
            assert self.head == self.tail
        elif self.length == 2:
            assert self.head.next == self.tail
        else:
            actual_lst_len = 0
            temp_head = self.head

            while temp_head is not None:
                temp_head = temp_head.next
                actual_lst_len += 1
                assert actual_lst_len < 1000  # Consider infinite cycle

            assert self.length == actual_lst_len
            assert self.length == len(self.debug_data)

    ##############################################

    def insert_end(self, value):
        node = Node(value)
        self._add_node(node)

        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.debug_verify_data_integrity()  # ** verify as possible

    def print(self):
        temp_head = self.head

        while temp_head is not None:
            print(temp_head.data, end='->')
            temp_head = temp_head.next
        print('None')

    def __iter__(self):
        temp_head = self.head
        while temp_head is not None:
            yield temp_head
            temp_head = temp_head.next

    def __repr__(self):
        represent = ''
        temp_head = self.head

        while temp_head is not None:
            represent += str(temp_head.data)
            temp_head = temp_head.next
            if temp_head:
                represent += ', '

        return represent

    ##############################################

    def insert_front(self, value):  # O(1) time - O(1) memory
        item = Node(value)
        self._add_node(item)

        item.next = self.head
        self.head = item

        if self.length == 1:
            self.tail = self.head

        self.debug_verify_data_integrity()

    def delete_front(self):                 # O(1) time - O(1) memory
        if not self.head:
            return

        next = self.head.next
        self._delete_node(self.head)
        self.head = next

        if self.length <= 1:
            self.tail = self.head

        self.debug_verify_data_integrity()

    def add_num(self, another_lst):
        # let X = max(length, another_lst.length)
        # let Y = max(length, another_lst.length) - min(length, another_lst.length)
        # O(X) time and O(Y) memory
        if not another_lst.length:
            return

        cur1, cur2 = self.head, another_lst.head
        carry = 0

        # Iterate on both in the same time: add l2's node value to l1's node value
        while cur1 or cur2:
            value1, value2 = 0, 0
            if cur1:
                value1 = cur1.data
            if cur2:
                value2 = cur2.data
                cur2 = cur2.next

            value1 += value2 + carry
            carry = value1 // 10
            value1 %= 10

            if cur1:   # put new value
                cur1.data = value1
                cur1 = cur1.next
            else:       # first ended, keep adding the values of the 2nd
                self.insert_end(value1)
            # we can even stop earlier
        if carry:
            self.insert_end(carry)
        self.debug_verify_data_integrity()


def test1():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst1 = LinkedList([])
    lst2 = LinkedList([])
    lst1.add_num(lst2)

    lst1.debug_print_existing_nodes()
    result = str(lst1)
    expected = ''

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test2():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst1 = LinkedList([1, 2, 3])
    lst2 = LinkedList([4, 5, 6])
    lst1.add_num(lst2)

    lst1.debug_print_existing_nodes()
    result = str(lst1)
    expected = '5, 7, 9'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test3():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst1 = LinkedList([])
    lst2 = LinkedList([3, 5, 4])
    lst1.add_num(lst2)

    lst1.debug_print_existing_nodes()
    result = str(lst1)
    expected = '3, 5, 4'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')



def test4():    # 98754678+569 = 98755247
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst1 = LinkedList([9, 6, 5])
    lst2 = LinkedList([8, 7, 6, 4, 5, 7, 8, 9])
    lst1.add_num(lst2)

    lst1.debug_print_existing_nodes()
    result = str(lst1)
    expected = '7, 4, 2, 5, 5, 7, 8, 9'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test5(): # 98754678+569 = 98755247
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst1 = LinkedList([9, 6, 5])
    lst2 = LinkedList([8, 7, 6, 4, 5, 7, 8, 9])
    lst1.add_num(lst2)

    lst1.debug_print_existing_nodes()
    result = str(lst1)
    expected = '7, 4, 2, 5, 5, 7, 8, 9'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')




if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()



