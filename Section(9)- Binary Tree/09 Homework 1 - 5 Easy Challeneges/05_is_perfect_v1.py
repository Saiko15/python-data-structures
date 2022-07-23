class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def add(self, values_lst, direction_lst):
        assert len(values_lst) == len(direction_lst)

        current = self.root
        # iterate on the path, all necessary nodes
        for i, val in enumerate(values_lst):
            if direction_lst[i] == 'L':
                if not current.left:
                    current.left = Node(values_lst[i])
                else:
                    assert current.left.data == values_lst[i]
                current = current.left
            else:
                if not current.right:
                    current.right = Node(values_lst[i])
                else:
                    assert current.right.data == values_lst[i]
                current = current.right


    ##################################
    def _tree_height(self, current):
        if not current:
            return -1

        return 1 + max(self._tree_height(current.left), self._tree_height(current.right))

    def tree_height(self):
        return self._tree_height(self.root)

    def _is_perfect(self, current, height):
        if not current.left and not current.right:
            return height == 0

        if not current.left and current.right:
            return False

        if current.left and not current.right:
            return False

        return self._is_perfect(current.left, height - 1) and \
               self._is_perfect(current.right, height - 1)

    def is_perfect(self):
        h = self.tree_height()
        return self._is_perfect(self.root, h)




if __name__ == '__main__':
    tree = BinaryTree(1)

    assert tree.is_perfect()

    tree.add([2], ['L'])
    assert not tree.is_perfect()

    tree.add([3], ['R'])
    assert tree.is_perfect()

    tree.add([2, 4, 7], ['L', 'L', 'L'])
    tree.add([2, 4, 8], ['L', 'L', 'R'])
    tree.add([2, 5, 9], ['L', 'R', 'R'])
    tree.add([3, 6, 15], ['R', 'R', 'L'])
    assert not tree.is_perfect()

    tree.add([2, 5, 13], ['L', 'R', 'L'])
    tree.add([3, 6, 12], ['R', 'R', 'R'])
    tree.add([3, 14, 15], ['R', 'L', 'L'])
    tree.add([3, 14, 16], ['R', 'L', 'R'])
    assert tree.is_perfect()

