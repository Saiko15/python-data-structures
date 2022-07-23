# https://leetcode.com/problems/cousins-in-binary-tree/

class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
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
                    assert current.left.val == values_lst[i]
                current = current.left
            else:
                if not current.right:
                    current.right = Node(values_lst[i])
                else:
                    assert current.right.val == values_lst[i]
                current = current.right


class Solution(object):
    def find(self, root, parent, value, depth=0):
        # Find node with the request value and return its parent node
        if not root:
            return None, depth

        if root.val == value:
            return parent, depth

        lparent, ldepth = self.find(root.left, root, value, depth+1)

        if lparent:
            return lparent, ldepth

        return self.find(root.right, root, value, depth+1)

    def isCousins(self, root, x, y):
        xparent, xdepth = self.find(root, None, x)
        yparent, ydepth = self.find(root, None, y)

        return xdepth == ydepth and xparent != yparent


if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.add([2, 4, 7], ['L', 'L', 'L'])
    tree.add([2, 4, 8], ['L', 'L', 'R'])
    tree.add([2, 5, 9], ['L', 'R', 'R'])
    tree.add([3, 6, 15], ['R', 'R', 'L'])

    sol = Solution()

