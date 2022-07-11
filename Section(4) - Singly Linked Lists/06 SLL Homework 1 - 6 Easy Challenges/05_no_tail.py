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

        if initial_values:
            for value in initial_values:
                self.add_element(value)

    def add_element(self, value):
        item = Node(value)
        item.next = self.head
        self.head = item

    def get_tail(self):
        temp_head = self.head

        while temp_head is not None and temp_head.next is not None:
            temp_head = temp_head.next

        return temp_head

    def __repr__(self):
        represent = ''
        temp_head = self.head

        while temp_head is not None:
            represent += str(temp_head.data)
            temp_head = temp_head.next
            if temp_head:
                represent += ', '

        return represent


def test1():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([])
    result = str(lst)
    expected = ''

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test2():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([1, 2, 3])
    result = str(lst)
    expected = '3, 2, 1'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'

    assert lst.get_tail().data == 1

    print('PASSED\n')


if __name__ == '__main__':
    test1()
    test2()

    # Must see to insure no RTE
    print('ALL CASES PASSED')

