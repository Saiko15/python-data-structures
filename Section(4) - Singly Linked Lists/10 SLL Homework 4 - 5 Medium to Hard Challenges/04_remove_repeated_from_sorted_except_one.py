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

    def get_nth_back(self, n):  # O(n) time - O(1) memory
        # If we know the length, we can compute its normal position
        if self.length < n:
            return None

        # Provideits 1-based index from forward
        return self.get_nth(self.length - n + 1)

    def is_identical_data(self, other):  # O(n) time - O(1) memory
        h1, h2 = self.head, other.head

        while h1 and h2:
            if h1.data != h2.data:
                return False
            h1, h2 = h1.next, h2.next

        # make sure both ends together
        return not h1 and not h2

    #######################################

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

    def delete_nth_node(self, n):
        if n < 1 or n > self.length:
            print("Error. No such nth node")
        elif n == 1:
            self.delete_front()
        else:
            # Connect the node before nth with node after nth
            before_nth = self.get_nth(n - 1)
            nth = before_nth.next
            is_nth_tail = nth == self.tail
            # connect before node with after
            before_nth.next = nth.next

            if is_nth_tail:
                self.tail = before_nth

            self._delete_node(nth)
            self.debug_verify_data_integrity()

    ####################################
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

        cur = self.head
        while cur and cur.next:
            if cur.data == cur.next.data:
                self._delete_next_node(cur)
            else:
                cur = cur.next



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

    lst = LinkedList([10, 20])
    lst.delete_all_repeated_from_sorted()

    lst.debug_print_existing_nodes()
    result = str(lst)
    expected = '10, 20'

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
    expected = '1'

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
    expected = '1, 2'

    assert result == expected, \
        f'Mismatch between expected=[{expected}] ' \
        f'and result=[{result}] in {func_name}'
    print('PASSED\n')


def test6():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([1, 1, 2, 3])
    lst.delete_all_repeated_from_sorted()

    lst.debug_print_existing_nodes()
    result = str(lst)
    expected = '1, 2, 3'

    assert result == expected, \
        f'Mismatch between expected=[{expected}] ' \
        f'and result=[{result}] in {func_name}'
    print('PASSED\n')


def test7():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([1, 2, 3, 3, 3, 3])
    lst.delete_all_repeated_from_sorted()

    lst.debug_print_existing_nodes()
    result = str(lst)
    expected = '1, 2, 3'

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
    expected = '1, 2, 3'

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


    def delete_node_with_key(self, value):
        # O(n) time - O(1) memory
        if not self.length:
            return

        if self.head.data == value:
            self.delete_front()
        else:
            prev, cur = None, self.head
            while cur:
                if cur.data == value:
                    self._delete_next_node(prev)
                    break
                prev, cur = cur, cur.next

        self.debug_verify_data_integrity()

    def swap_pairs(self):
        temp_head = self.head

        while temp_head is not None and temp_head.next is not None:
            temp_head.data, temp_head.next.data = temp_head.next.data, temp_head.data
            temp_head = temp_head.next.next

        self.debug_verify_data_integrity()

    def reverse(self):  # O(n) time - O(1) memory
        if self.length <= 1:
            return

        self.tail = self.head
        prv = self.head
        self.head = self.head.next
        while self.head:
            # store & reverse link
            next = self.head.next
            self.head.next = prv
            # move step
            prv = self.head
            self.head = next

        # Finalize self.head and self.tail
        self.head = prv
        self.tail.next = None
        self.debug_verify_data_integrity()

    def delete_even_positions(self): 		# O(n) time - O(1) memory
        if self.length <= 1:
            return
        # use the first 2 nodes
        prev, cur = self.head, self.head.next
        while cur:
            # prev is odd, prev-next is even
            self._delete_next_node(prev)
            if not prev.next: # if tail
                break
            cur = prev.next.next
            prev = prev.next

        self.debug_verify_data_integrity()

    def _embed_after(self, node, value):
        # Add a node with value between node and its next
        new_node = Node(value)
        self._add_node(new_node)
        new_node.next = node.next
        node.next = new_node

    def insert_sorted(self, value): 		# O(n) time - O(1) memory
        # 3 special cases for simplicity
        if not self.length or value <= self.head.data:
            self.insert_front(value)
        elif self.tail.data <= value:
            self.insert_end(value)
        else:
            prev, cur = None, self.head
            while cur:
                if value <= cur.data:
                    self._embed_after(prev, value)
                    break
                prev, cur = cur, cur.next

        self.debug_verify_data_integrity()
        # This idea is used in Insertion Sort Algorithm

    ##################
    def _get_previous(self, target):  # O(n) time - O(1) memory
        prev, cur = None, self.head
        while cur:
            if cur == target:
                return prev
            prev, cur = cur, cur.next
        return None

    def swap_head_tail(self):  # O(n) time - O(1) memory
        if self.length <= 1:
            return

        if self.length == 2:
            self.head, self.tail = self.tail, self.head  # Swap
            self.head.next = self.tail
            self.tail.next = None
            return

        prv = self._get_previous(self.tail)

        # Let's make current tail as self.head
        # Link tail to the 2nd node
        self.tail.next = self.head.next

        # Let's make current self.head as tail
        # Link tail's previous to self.head
        prv.next = self.head
        self.head.next = None

        self.head, self.tail = self.tail, self.head  # Swap

        self.debug_verify_data_integrity()

    def left_rotate(self, k): 		# O(n) time - O(1) memory
        if self.length <= 1 or k % self.length == 0:
            return	# 0 or 1 elements or useless rotation
        k %= self.length	# Remove useless cycles

        nth = self.get_nth(k)
        self.tail.next = self.head		# create cycle

        # Reset self.tail/self.head
        self.tail = nth
        self.head = nth.next

        self.tail.next = None	# disconnect cycle
        self.debug_verify_data_integrity()

    def remove_duplicates_from_not_sorted(self):  # O(n^2) time - O(1) memory
        if self.length <= 1:
            return

        # Just like 2 nested loops, find all duplicates and delete
        cur1 = self.head
        while cur1:
            prev2, cur2 = cur1, cur1.next
            while cur2:
                if cur1.data == cur2.data:
                    self._delete_next_node(prev2)
                    cur2 = prev2.next
                else:
                    prev2, cur2 = cur2, cur2.next
            # Tip: we can also easily code it without previous node
            # Tip: With hashing technique (later), this can be in O(n) time / O(n) memory
            cur1 = cur1.next

    def delete_last_occurrence_target(self, target):  # O(n) time - O(1) memory
        if self.length <= 1:
            return

        delete_my_next_node = None
        is_found = False

        # Find the last one and keep its previous
        prev, cur = None, self.head
        while cur:
            if cur.data == target:  # each time find it:
                delete_my_next_node = prev
                is_found = True
            prev, cur = cur, cur.next

        if is_found:
            if delete_my_next_node:
                self._delete_next_node(delete_my_next_node)
            else: # if last prv is null, found at self.head
                self.delete_front()

        self.debug_verify_data_integrity()

    def _move_to_end(self, cur, prv):
        # Move cur after the tail and return its next
        next = cur.next
        self.tail.next = cur

        if prv:
            prv.next = next
        else:
            self.head = next  # cur was self.head

        self.tail = cur
        self.tail.next = None
        return next

    def move_key_occurance_to_end(self, target):  # O(n) time - O(1) memory
        if self.length <= 1:
            return

        # For each matching key, move it to the end!
        # But, be careful from infinite loop. Iterate maximum self.length
        len = self.length
        prev, cur = None, self.head

        while cur and len:
            if cur.data == target:
                cur = self._move_to_end(cur, prev)
            else:
                prev, cur = cur, cur.next
            len -= 1

        self.debug_verify_data_integrity()

    ##########################################
    def odd_pos_even_pos(self):  # O(n) time - O(1) memory
        if self.length <= 2:
            return

        first_even = self.head.next
        cur_odd = self.head

        while cur_odd.next and cur_odd.next.next:
            next_even = cur_odd.next
            # connect odd with odd and even with even
            cur_odd.next = cur_odd.next.next
            next_even.next = next_even.next.next
            cur_odd = cur_odd.next
            # for odd self.length, is changed to last even node
            if self.length % 2 == 1:
                self.tail = next_even

        # connect last odd with the first even
        cur_odd.next = first_even
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

        # Iterate on both in the same time: add l2's node after l1's node
        cur1, cur2 = self.head, another_lst.head
        while cur1 and cur2:
            cur2 = insert_after(cur1, cur2)

            if cur1 == self.tail:   # If first lst ended early, then tail comes from list 2
                self.tail = another_lst.tail
                cur1.next.next = cur2   # link with the remaining
                break

            cur1 = cur1.next.next

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

    def delete_all_repeated_from_sorted(self):  # O(n) time - O(1) memory
        if self.length <= 1:
            return

        cur = self.head
        while cur and cur.next:
            if cur.data == cur.next.data:
                self._delete_next_node(cur)
            else:
                cur = cur.next



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

    lst = LinkedList([10, 20])
    lst.delete_all_repeated_from_sorted()

    lst.debug_print_existing_nodes()
    result = str(lst)
    expected = '10, 20'

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
    expected = '1'

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
    expected = '1, 2'

    assert result == expected, \
        f'Mismatch between expected=[{expected}] ' \
        f'and result=[{result}] in {func_name}'
    print('PASSED\n')


def test6():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([1, 1, 2, 3])
    lst.delete_all_repeated_from_sorted()

    lst.debug_print_existing_nodes()
    result = str(lst)
    expected = '1, 2, 3'

    assert result == expected, \
        f'Mismatch between expected=[{expected}] ' \
        f'and result=[{result}] in {func_name}'
    print('PASSED\n')


def test7():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([1, 2, 3, 3, 3, 3])
    lst.delete_all_repeated_from_sorted()

    lst.debug_print_existing_nodes()
    result = str(lst)
    expected = '1, 2, 3'

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
    expected = '1, 2, 3'

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
