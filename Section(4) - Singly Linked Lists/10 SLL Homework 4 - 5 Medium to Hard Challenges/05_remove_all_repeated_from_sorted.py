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

    def get_nth(self, n):       # O(n) time - O(1) memory
        temp_head = self.head
        cnt = 1

        while temp_head is not None:
            if cnt == n:
                return temp_head
            temp_head = temp_head.next
            cnt += 1
        return None
    
    def delete_last(self):
        if self.length <= 1:
            self.delete_front()
            return

        # Tail is at length-1
        previous = self.get_nth(self.length - 1)

        self._delete_node(self.tail)
        self.tail = previous
        self.tail.next = None

        self.debug_verify_data_integrity()

    def _delete_next_node(self, node):
        to_delete = node.next
        assert to_delete is not None

        is_tail = to_delete == self.tail
        # node.next in middle to delete
        node.next = node.next.next
        self._delete_node(to_delete)

        if is_tail:
            self.tail = node

    def delete_all_repeated_from_sorted(self):  # O(n) time - O(1) memory
        if self.length <= 1:
            return
        # dummy head and tail for easy handling - keep this trick in MIND
        self.insert_front(self.head.data - 1)
        self.insert_end(self.tail.data + 1)

        # we can develop with 2 nested while loops. Here a simpler logic
        prev, cur = self.head, self.head.next
        last_removed_value = self.head.data - 1

        while cur and cur.next:
            if cur.data == cur.next.data:
                last_removed_value = cur.data
                self._delete_next_node(cur)
            else:
                if last_removed_value == cur.data:  # delete first too
                    self._delete_next_node(prev)
                    cur = prev
                prev, cur = cur, cur.next

        self.delete_front() # undo dumy
        self.delete_last()



def test1():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([])
    lst.delete_all_repeated_from_sorted()

    lst.debug_print_existing_nodes()
    result = str(lst)
    expected = ''

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test2():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([10])
    lst.delete_all_repeated_from_sorted()

    lst.debug_print_existing_nodes()
    result = str(lst)
    expected = '10'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test3():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([1, 1])
    lst.delete_all_repeated_from_sorted()

    lst.debug_print_existing_nodes()
    result = str(lst)
    expected = ''

    assert result == expected, \
        f'Mismatch between expected=[{expected}] ' \
        f'and result=[{result}] in {func_name}'
    print('PASSED\n')


def test4():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([1, 1, 1])
    lst.delete_all_repeated_from_sorted()

    lst.debug_print_existing_nodes()
    result = str(lst)
    expected = ''

    assert result == expected, \
        f'Mismatch between expected=[{expected}] ' \
        f'and result=[{result}] in {func_name}'
    print('PASSED\n')


def test5():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([1, 1, 2, 2])
    lst.delete_all_repeated_from_sorted()

    lst.debug_print_existing_nodes()
    result = str(lst)
    expected = ''

    assert result == expected, \
        f'Mismatch between expected=[{expected}] ' \
        f'and result=[{result}] in {func_name}'
    print('PASSED\n')


def test6():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([1, 1, 2, 3, 3, 4, 4, 5, 6])
    lst.delete_all_repeated_from_sorted()

    lst.debug_print_existing_nodes()
    result = str(lst)
    expected = '2, 5, 6'

    assert result == expected, \
        f'Mismatch between expected=[{expected}] ' \
        f'and result=[{result}] in {func_name}'
    print('PASSED\n')


def test7():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([1, 1, 2, 3, 3, 4, 4, 5, 6, 7, 7])
    lst.delete_all_repeated_from_sorted()

    lst.debug_print_existing_nodes()
    result = str(lst)
    expected = '2, 5, 6'

    assert result == expected, \
        f'Mismatch between expected=[{expected}] ' \
        f'and result=[{result}] in {func_name}'
    print('PASSED\n')


def test8():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([1, 2, 2, 2, 2, 3, 3, 3, 3])
    lst.delete_all_repeated_from_sorted()

    lst.debug_print_existing_nodes()
    result = str(lst)
    expected = '1'

    assert result == expected, \
        f'Mismatch between expected=[{expected}] ' \
        f'and result=[{result}] in {func_name}'
    print('PASSED\n')


def test9():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([1, 2, 3, 4])
    lst.delete_all_repeated_from_sorted()

    lst.debug_print_existing_nodes()
    result = str(lst)
    expected = '1, 2, 3, 4'

    assert result == expected, \
        f'Mismatch between expected=[{expected}] ' \
        f'and result=[{result}] in {func_name}'
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
