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

    def insert_alternate(self, another_lst):  # O(n) time - O(1) memory
        self.debug_data.extend(another_lst.debug_data)

        if not another_lst.length:
            return
        if not self.length:  # move head and tail
            self.head = another_lst.head
            self.tail = another_lst.tail
            self.length += another_lst.length
            return

        self.length += another_lst.length

        def insert_after(src, target):
            # Given 2 nodes: src and target
            # Insert target after src and link properly
            # [1, 2, 4, 5]: src = 2 and target 3 ==> [1, 2, 3, 4, 5]
            next = cur2.next
            target.next = src.next
            src.next = target
            return next

        # Iterate one by one on both list and insert lst2 node after lst1 node
        cur1, cur2 = self.head, another_lst.head
        while cur1 and cur2:
            cur2 = insert_after(cur1, cur2)

            if cur1 == self.tail:   # If first lst ended early, then tail comes from list 2
                self.tail = another_lst.tail
                cur1.next.next = cur2   # link with the remaining
                break

            cur1 = cur1.next.next

        self.debug_verify_data_integrity()


def test1():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst1 = LinkedList([])
    lst2 = LinkedList([])
    lst1.insert_alternate(lst2)

    lst1.debug_print_existing_nodes()
    result = str(lst1)
    expected = ''

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test2():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst1 = LinkedList([10])
    lst2 = LinkedList([])
    lst1.insert_alternate(lst2)

    lst1.debug_print_existing_nodes()
    result = str(lst1)
    expected = '10'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test3():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst1 = LinkedList([])
    lst2 = LinkedList([10])
    lst1.insert_alternate(lst2)

    lst1.debug_print_existing_nodes()
    result = str(lst1)
    expected = '10'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')



def test4():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst1 = LinkedList([1])
    lst2 = LinkedList([2])
    lst1.insert_alternate(lst2)

    lst1.debug_print_existing_nodes()
    result = str(lst1)
    expected = '1, 2'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test5():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst1 = LinkedList([1, 2])
    lst2 = LinkedList([3])
    lst1.insert_alternate(lst2)

    lst1.debug_print_existing_nodes()
    result = str(lst1)
    expected = '1, 3, 2'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test6():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst1 = LinkedList([1])
    lst2 = LinkedList([2, 3])
    lst1.insert_alternate(lst2)

    lst1.debug_print_existing_nodes()
    result = str(lst1)
    expected = '1, 2, 3'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test7():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst1 = LinkedList([1, 2, 3])
    lst2 = LinkedList([4, 5, 6])
    lst1.insert_alternate(lst2)

    lst1.debug_print_existing_nodes()
    result = str(lst1)
    expected = '1, 4, 2, 5, 3, 6'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test8():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst1 = LinkedList([1, 2, 3])
    lst2 = LinkedList([])
    lst1.insert_alternate(lst2)

    lst1.debug_print_existing_nodes()
    result = str(lst1)
    expected = '1, 2, 3'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test9():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst1 = LinkedList([])
    lst2 = LinkedList([1, 2, 3])
    lst1.insert_alternate(lst2)

    lst1.debug_print_existing_nodes()
    result = str(lst1)
    expected = '1, 2, 3'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test10():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst1 = LinkedList([1, 2, 3])
    lst2 = LinkedList([4, 5, 6, 7, 8])
    lst1.insert_alternate(lst2)

    lst1.debug_print_existing_nodes()
    result = str(lst1)
    expected = '1, 4, 2, 5, 3, 6, 7, 8'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
    test10()


