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

    def _total_nodes(self, current):
        if not current:
            return 0

        return 1 + self._total_nodes(current.left) + self._total_nodes(current.right)

    def is_perfect(self):
        h = self._tree_height(self.root)
        n = self._total_nodes(self.root)
        p = 2 ** (h + 1)
        return n == p-1




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

