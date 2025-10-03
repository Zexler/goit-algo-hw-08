#!/usr/bin/env python3

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return AVLNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node
        node.update_height()
        return self._balance_node(node)

    def _balance_node(self, node):
        balance = node.get_balance()
        if balance < -1:
            if node.right.get_balance() > 0:
                node.right = node.right.rotate_right()
            return node.rotate_left()
        if balance > 1:
            if node.left.get_balance() < 0:
                node.left = node.left.rotate_left()
            return node.rotate_right()
        return node

    def __str__(self):
        return str(self.root) if self.root else "Empty tree"


class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = self.right = None

    def update_height(self):
        left_h = self.left.height if self.left else 0
        right_h = self.right.height if self.right else 0
        self.height = 1 + max(left_h, right_h)

    def get_balance(self):
        left_h = self.left.height if self.left else 0
        right_h = self.right.height if self.right else 0
        return left_h - right_h

    def rotate_left(self):
        if not self.right:
            return self
        new_root = self.right
        self.right = new_root.left
        new_root.left = self
        self.update_height()
        new_root.update_height()
        return new_root

    def rotate_right(self):
        if not self.left:
            return self
        new_root = self.left
        self.left = new_root.right
        new_root.right = self
        self.update_height()
        new_root.update_height()
        return new_root

    def __str__(self, level=0, prefix="Root: "):
        result = "  " * level + prefix + str(self.key) + f" (h={self.height})\n"
        if self.left:
            result += self.left.__str__(level + 1, "L-- ")
        if self.right:
            result += self.right.__str__(level + 1, "R-- ")
        return result


def insert_avl(root, key):
    if root is None:
        return AVLNode(key)
    tree = AVLTree()
    tree.root = root
    tree.insert(key)
    return tree.root

class BinarySearchTree:
    def __init__(self, root_value=None):
        self.root = BinaryNode(root_value) if root_value is not None else None

    def insert(self, value):
        if not self.root:
            self.root = BinaryNode(value)
        else:
            self.root.insert(value)

    def search(self, value):
        return self.root.search(value) if self.root else False

    def find_min(self):
        return self.root.find_min() if self.root else None

    def find_max(self):
        return self.root.find_max() if self.root else None

    def __str__(self):
        return str(self.root) if self.root else "Empty BST"


class BinaryNode:
    def __init__(self, value):
        self.val = value
        self.left = self.right = None

    def insert(self, value):
        if value < self.val:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinaryNode(value)
        elif value > self.val:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinaryNode(value)

    def search(self, value):
        if value == self.val:
            return True
        return (self.left.search(value) if value < self.val and self.left else
                self.right.search(value) if value > self.val and self.right else False)

    def find_min(self):
        current = self
        while current.left:
            current = current.left
        return current.val

    def find_max(self):
        current = self
        while current.right:
            current = current.right
        return current.val

    def __str__(self, level=0, prefix="Root: "):
        result = "  " * level + prefix + str(self.val) + "\n"
        if self.left:
            result += self.left.__str__(level + 1, "L-- ")
        if self.right:
            result += self.right.__str__(level + 1, "R-- ")
        return result


def insert_bst(root, key):
    if root is None:
        return BinaryNode(key)
    root.insert(key)
    return root

import heapq

def find_tree_min(tree_root):
    if not tree_root:
        return None
    current = tree_root
    while current.left:
        current = current.left
    return getattr(current, 'val', None) if getattr(current, 'val', None) is not None else getattr(current, 'key', None)

def calculate_tree_sum(root):
    if not root:
        return 0
    total = 0
    nodes = [root]
    while nodes:
        node = nodes.pop()
        value = getattr(node, 'val', None)
        if value is None:
            value = getattr(node, 'key', None)
        if value is not None:
            total += value
        if node.left:
            nodes.append(node.left)
        if node.right:
            nodes.append(node.right)
    return total

def connect_cables_min_cost(cable_lengths):
    if len(cable_lengths) <= 1:
        return 0
    cables = cable_lengths.copy()
    heapq.heapify(cables)
    total_cost = 0
    while len(cables) > 1:
        cost = heapq.heappop(cables) + heapq.heappop(cables)
        total_cost += cost
        heapq.heappush(cables, cost)
    return total_cost

def get_min_node_value(node): return find_tree_min(node)
def sum_tree(root): return calculate_tree_sum(root)
def min_cost_cables(lengths): return connect_cables_min_cost(lengths)

def print_task_header(n: int):
    label = f" ЗАДАЧА {n} "
    width = len(label)
    print("┌" + "─" * width + "┐")
    print("│" + label + "│")
    print("└" + "─" * width + "┘")

def demo_avl_tree():
    print("AVL-дерево")
    avl = AVLTree()
    values = [10, 20, 5, 8, 3, 4, 2]
    print(f"Вхідні: {values}")
    for i, val in enumerate(values, 1):
        avl.insert(val)
        print(f"{i}) +{val}; мін={find_tree_min(avl.root)}")
    print("Структура:")
    print(avl)
    total = calculate_tree_sum(avl.root)
    print(f"Сума вузлів: {total}")
    return avl.root

def demo_bst():
    print("BST (бінарне дерево пошуку)")
    bst = BinarySearchTree(50)
    values = [30, 20, 40, 70, 58, 80]
    print(f"Корінь=50; додаємо: {values}")
    for i, val in enumerate(values, 1):
        bst.insert(val)
        print(f"{i}) +{val} ✓")
    print("Структура:")
    print(bst)
    print(f"Діапазон: {bst.find_min()}–{bst.find_max()}")
    print(f"Сума вузлів: {calculate_tree_sum(bst.root)}")
    return bst.root

def demo_cable_connection():
    print("З'єднання кабелів — мінімальна вартість")
    test_cases = [
        ([4, 3, 2, 6], "базовий"),
        ([8, 4, 6, 12], "змішані"),
        ([5, 5, 5, 5], "однакові"),
        ([1, 2], "два"),
        ([10], "один"),
        ([], "порожньо")
    ]
    for i, (cables, tag) in enumerate(test_cases, 1):
        cost = connect_cables_min_cost(cables)
        print(f"{i}) {tag}: {cables if cables else '[]'} → {cost}")

def main():
    print("Демонстрація алгоритмів і структур даних\n")

    print_task_header(1)
    avl_root = demo_avl_tree()
    print()

    bst_root = demo_bst()
    print()

    print_task_header(2)
    print("Суми вузлів")
    print(f"AVL: {calculate_tree_sum(avl_root)}")
    print(f"BST: {calculate_tree_sum(bst_root)}")
    print()

    print_task_header(3)
    demo_cable_connection()
    print("\nГотово.")

if __name__ == "__main__":
    main()
