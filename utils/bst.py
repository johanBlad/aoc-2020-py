class Node:
    def __init__(self, value):
        self.value = value
        self.l = None
        self.r = None


class Tree:
    root: Node

    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(value, self.root)

    def _add(self, new_value: int, node: Node):
        if new_value <= node.value:
            if node.l is None:
                node.l = Node(new_value)
            else:
                self._add(new_value, node.l)
        else:
            if node.r is None:
                node.r = Node(new_value)
            else:
                self._add(new_value, node.r)

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, find_value, node):
        if find_value == node.value:
            return node.value
        elif find_value <= node.value and node.l is not None:
            return self._find(find_value, node.l)
        elif find_value > node.value and node.r is not None:
            return self._find(find_value, node.r)

    def print_tree_sorted(self):
        if self.root is not None:
            self._print_tree_sorted(self.root)

    def _print_tree_sorted(self, node):
        if node is not None:
            self._print_tree_sorted(node.l)
            print(str(node.value) + " ")
            self._print_tree_sorted(node.r)

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        return max(self._height(node.l), self._height(node.r)) + 1

    # def print_tree_struct(self):
    #     if self.root is not None:
    #         self._print_tree_struct(self.root)

    # def _print_tree_struct(self, node):
    #     print(node.value)

    def populate_tree(self, values):
        if len(values) == 0:
            return
        i_mid = len(values) // 2

        self.add(values[i_mid])

        self.populate_tree(values[:i_mid])
        self.populate_tree(values[i_mid + 1 :])
