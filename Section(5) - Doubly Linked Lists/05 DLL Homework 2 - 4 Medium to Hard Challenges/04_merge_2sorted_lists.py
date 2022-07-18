import inspect


class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

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

    def debug_print_address(self):
        cur = self.head

        while cur is not None:
            print(f'{cur.data}@{id(cur)}', end='\t->\t')
            cur = cur.next
        print('None')

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

        prev_value = 'None' if node.prev is None else str(node.prev.data)
        print(prev_value.ljust(5), end='\t')

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
        assert self.head.prev is None
        assert self.tail is not None
        assert self.tail.next is None

        if self.length == 1:
            assert self.head == self.tail
        elif self.length == 2:
            assert self.head.next == self.tail
        else:
            assert self.length == len(self.debug_data)

            # Verify forward pass
            actual_lst_len = 0
            cur = self.head

            while cur is not None:
                cur = cur.next
                actual_lst_len += 1
                assert actual_lst_len < 1000  # Consider infinite cycle

            assert self.length == actual_lst_len
            
            # Verify backward pass 
            actual_lst_len = 0
            cur = self.tail

            while cur is not None:
                cur = cur.prev
                actual_lst_len += 1
                assert actual_lst_len < 1000  # Consider infinite cycle

            assert self.length == actual_lst_len

    ##############################################
    def print(self):
        cur = self.head

        while cur is not None:
            print(cur.data, end='->')
            cur = cur.next
        print('None')

    def print_reversed(self):
        cur = self.tail

        while cur is not None:
            print(cur.data, end='->')
            cur = cur.prev
        print('None')

    def __iter__(self):
        cur = self.head
        while cur is not None:
            yield cur
            cur = cur.next

    def __repr__(self):
        represent = ''
        cur = self.head

        while cur is not None:
            represent += str(cur.data)
            cur = cur.next
            if cur:
                represent += ', '

        return represent
    ##############################################
    @staticmethod
    def _link(first, second):
        if first:
            first.next = second
        if second:
            second.prev = first

    def insert_end(self, value):
        node = Node(value)
        self._add_node(node)

        if not self.head:
            self.head = self.tail = node
        else:
            self._link(self.tail, node)
            self.tail = node

        self.debug_verify_data_integrity()

    def insert_front(self, value):
        item = Node(value)
        self._add_node(item)

        self._link(item, self.head)
        self.head = item

        if self.length == 1:
            self.tail = self.head

        self.debug_verify_data_integrity()

    def delete_front(self):
        if not self.head:
            return

        next = self.head.next
        self._delete_node(self.head)
        self.head = next

        if self.head:
            self.head.prev = None

        if self.length <= 1:
            self.tail = self.head

        self.debug_verify_data_integrity()

    def delete_last(self):
        if self.length <= 1:
            self.delete_front()
            return

        #previous = self.get_nth(self.length - 1)
        previous = self.tail.prev

        self._delete_node(self.tail)
        self.tail = previous
        self.tail.next = None

        self.debug_verify_data_integrity()

    def _delete_link_node(self, node):
        if not node:
            return
        is_tail = node == self.tail
        prev = node.prev
        self._link(prev, node.next)
        self._delete_node(node)

        if is_tail:
            self.tail = prev

        return prev

    def delete_node_with_key(self, key):
        if not self.length:
            return

        if self.head.data == key:
            self.delete_front()
        else:
            cur = self.head
            while cur:
                if cur.data == key:
                    self._delete_link_node(cur)
                    break
                cur = cur.next

        self.debug_verify_data_integrity()

    def merge_2sorted_list(self, other):  # On+m
        if not other.head:
            return

        if self.head:
            cur1, cur2 = self.head, other.head
            self.head = last = None

            while cur1 and cur2:
                # pick the smallest among the 2 lists and then link
                if cur1.data <= cur2.data:
                    next = cur1
                    cur1 = cur1.next
                else:
                    next = cur2
                    cur2 = cur2.next

                self._link(last, next)
                last = next
                if not self.head:  # first step
                    self.head = last

            if cur2:  # our self.tail is from 2nd
                self.tail = other.tail
                self._link(last, cur2)
            elif cur1:
                self._link(last, cur1)

        else:  # use its data
            self.head = other.head
            self.tail = other.tail

        self.length += other.length
        self.debug_data.extend(other.debug_data)

        self.debug_verify_data_integrity()



def test1():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst1 = LinkedList([10, 20, 30, 40, 50])
    lst2 = LinkedList([15, 17, 22, 24, 35])

    lst1.merge_2sorted_list(lst2)
    lst1.debug_print_existing_nodes()

    result = str(lst1)
    expected = '10, 15, 17, 20, 22, 24, 30, 35, 40, 50'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test2():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst1 = LinkedList([10, 20, 30, 40, 50])
    lst2 = LinkedList([5, 17, 22, 24, 60])

    lst1.merge_2sorted_list(lst2)
    lst1.debug_print_existing_nodes()

    result = str(lst1)
    expected = '5, 10, 17, 20, 22, 24, 30, 40, 50, 60'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test3():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst1 = LinkedList([10, 20, 30, 40, 50])
    lst2 = LinkedList([60])

    lst1.merge_2sorted_list(lst2)
    lst1.debug_print_existing_nodes()

    result = str(lst1)
    expected = '10, 20, 30, 40, 50, 60'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test4():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst1 = LinkedList([60])
    lst2 = LinkedList([10, 20, 30, 40, 50])

    lst1.merge_2sorted_list(lst2)
    lst1.debug_print_existing_nodes()

    result = str(lst1)
    expected = '10, 20, 30, 40, 50, 60'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test5():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst1 = LinkedList([])
    lst2 = LinkedList([10, 20, 30, 40, 50])

    lst1.merge_2sorted_list(lst2)
    lst1.debug_print_existing_nodes()

    result = str(lst1)
    expected = '10, 20, 30, 40, 50'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test6():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst1 = LinkedList([10, 20, 30, 40, 50])
    lst2 = LinkedList([])

    lst1.merge_2sorted_list(lst2)
    lst1.debug_print_existing_nodes()

    result = str(lst1)
    expected = '10, 20, 30, 40, 50'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')



if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()

    # Must see to insure no RTE
    print('ALL CASES PASSED')

