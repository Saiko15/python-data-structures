import ctypes


class Array:
    def __init__(self, size):
        self.size = size  # user size
        self._capacity = max(16, 2 * size)  # actual memory size

        array_data_type = ctypes.py_object * self._capacity
        self.memory = array_data_type()

        for i in range(self._capacity):
            self.memory[i] = None

    def expand_capacity(self):
        # Double the actual array size
        self._capacity *= 2
        print(f'Expand capacity to {self._capacity}')

        # create a new array of _capacity
        array_data_type = ctypes.py_object * self._capacity
        new_memory = array_data_type()

        for i in range(self.size):  # copy
            new_memory[i] = self.memory[i]

        # use the new memory and delete old one
        del self.memory
        self.memory = new_memory

    def append(self, item):
        if self.size == self._capacity:
            self.expand_capacity()
        self.memory[self.size] = item
        self.size += 1

    def insert(self, idx, item):
        if idx >= self.size:
            self.append(item)
            return
        if idx < -self.size:
            idx = -self.size
        if idx < 0:
            idx += self.size

        if self.size == self._capacity:
            # we can't add any more
            self.expand_capacity()

        # Shift all the data to right first CORRECTLY
        # Shift range (idx, size-1) from the back
        for p in range(self.size - 1, idx - 1, - 1):
            self.memory[p + 1] = self.memory[p]
        self.memory[idx] = item
        self.size += 1

        # Common mistake to iterate from begin to end
        # the whole array right array will be arr[idx]

    def right_rotate(self):
        if self.size == 0:
            return

        last_element = self.memory[self.size - 1]
        for idx in range(self.size - 2, - 1, - 1):
            self.memory[idx + 1] = self.memory[idx]
        self.memory[0] = last_element

    def left_rotate(self):
        if self.size == 0:
            return

        first_element = self.memory[0]
        for idx in range(1, self.size):
            self.memory[idx - 1] = self.memory[idx]
        self.memory[self.size - 1] = first_element

    def right_rotate_steps(self, times):
        times %= self.size
        for step in range(times):
            self.right_rotate()

    def pop(self, idx):
        assert idx >= -self.size and idx < self.size, 'pop index out of range'

        if idx < 0:
            idx += self.size

        val = self.memory[idx]

        # left shift the array
        # observe: if we remove the last a few values,
        # it will be very efficient due to few steps
        for p in range(idx + 1, self.size):
            self.memory[p - 1] = self.memory[p]

        self.size -= 1
        return val

    def index_transposition(self, value):
        for idx in range(self.size):
            if self.memory[idx] == value:
                if idx == 0:
                    return 0
                # Swap the 2 elements
                self.memory[idx], self.memory[idx - 1] = self.memory[idx - 1], self.memory[idx]
                return idx - 1
        return -1

    ############################

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        return self.memory[idx]  # Is valid idx?

    def __setitem__(self, idx, value):
        self.memory[idx] = value

    def __repr__(self):
        result = ''
        for i in range(self.size):
            result += str(self.memory[i]) + ', '
        return result


##################################################################################

def test_insert():
    array = Array(0)
    array.append(1)
    array.append(2)
    array.append(3)
    array.append(4)
    # 1, 2, 3, 4
    array.insert(-1, -10)
    print(array)  # 1, 2, 3, -10, 4,

    array.insert(-2, -20)
    print(array)  # 1, 2, 3, -20, -10, 4,

    array.insert(-3, -30)
    print(array)  # 1, 2, 3, -30, -20, -10, 4,

    array.insert(-4, -40)
    print(array)  # 1, 2, 3, -40, -30, -20, -10, 4,

    array.insert(-5, -50)
    print(array)  # 1, 2, 3, -50, -40, -30, -20, -10, 4,

    array.insert(8, 80)
    print(array)  # 1, 2, 3, -50, -40, -30, -20, -10, 80, 4,

    array.insert(20, 90)
    print(array)  # 1, 2, 3, -50, -40, -30, -20, -10, 80, 4, 90,


def test_right_rotate():
    array = Array(0)

    array.right_rotate()
    print(array)

    array = Array(0)
    array.append(0)
    array.append(1)
    array.append(2)
    array.append(3)
    array.append(4)

    array.right_rotate()
    print(array)
    # 4, 0, 1, 2, 3,

    array.right_rotate()
    print(array)
    # 3, 4, 0, 1, 2,


def test_left_rotate():
    array = Array(0)

    array.right_rotate()
    print(array)

    array = Array(0)
    array.append(0)
    array.append(1)
    array.append(2)
    array.append(3)
    array.append(4)

    array.left_rotate()
    print(array)
    # 1, 2, 3, 4, 0,

    array.left_rotate()
    print(array)
    # 2, 3, 4, 0, 1,


def test_right_rotate_steps():
    array = Array(0)
    array.append(0)
    array.append(1)
    array.append(2)
    array.append(3)
    array.append(4)
    print(array)
    # 0, 1, 2, 3, 4,

    array.right_rotate_steps(3)
    print(array)
    # 2, 3, 4, 0, 1,
    array.right_rotate_steps(7)
    print(array)
    # 0, 1, 2, 3, 4,

    array.right_rotate_steps(123456789)
    print(array)
    # 1, 2, 3, 4, 0,


def test_pop():
    array = Array(0)
    array.append(10)
    array.append(20)
    array.append(30)
    array.append(40)
    print(array)
    # 10, 20, 30, 40,

    print(array.pop(0))  # 10
    print(array)
    # 20, 30, 40,

    print(array.pop(2))  # 40
    print(array)
    # 20, 30,
    array.append(60)
    array.append(70)
    array.append(80)

    print(array.pop(-1))  # 80
    print(array)
    # 20, 30, 60, 70,

    print(array.pop(-4))  # 20
    print(array)
    # 30, 60, 70,
    # pop index out of range
    # array.pop(-4)
    # array.pop(3)


def test_index_transposition():

    array = Array(0)
    array.append(10)
    array.append(20)
    array.append(30)
    array.append(40)
    array.append(50)
    print(array)
    # 10, 20, 30, 40, 50,

    print(array.index_transposition(10))
    print(array)    # 0
    # 10, 20, 30, 40, 50,

    print(array.index_transposition(50))
    print(array)    # 3
    # 10, 20, 30, 50, 40,

    print(array.index_transposition(50))
    print(array)    # 2
    # 10, 20, 50, 30, 40,

    print(array.index_transposition(60))    # -1

if __name__ == '__main__':
    test_insert()
    # test_right_rotate
    # test_left_rotate()
    # test_right_rotate_steps()
    # test_pop()
	# test_index_transposition()
