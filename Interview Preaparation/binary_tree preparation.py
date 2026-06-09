# Interview preparation practice module.
# Contains core binary tree and BST interview algorithms.

from __future__ import annotations

from collections import deque


class Node:
    def __init__(self, val: int):
        self.val = val
        self.left: Node | None = None
        self.right: Node | None = None


def dfs_preorder_rec(root: Node | None) -> list[int]:
    if not root:
        return []
    return [root.val] + dfs_preorder_rec(root.left) + dfs_preorder_rec(root.right)


def dfs_inorder_rec(root: Node | None) -> list[int]:
    if not root:
        return []
    return dfs_inorder_rec(root.left) + [root.val] + dfs_inorder_rec(root.right)


def dfs_postorder_rec(root: Node | None) -> list[int]:
    if not root:
        return []
    return dfs_postorder_rec(root.left) + dfs_postorder_rec(root.right) + [root.val]


def level_order(root: Node | None) -> list[int]:
    if not root:
        return []
    q: deque[Node] = deque([root])
    order: list[int] = []
    while q:
        node = q.popleft()
        order.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return order


def max_depth_rec(root: Node | None) -> int:
    if not root:
        return 0
    return 1 + max(max_depth_rec(root.left), max_depth_rec(root.right))


def max_depth_iter(root: Node | None) -> int:
    if not root:
        return 0
    q: deque[Node] = deque([root])
    depth = 0
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        depth += 1
    return depth


def is_same_tree(p: Node | None, q: Node | None) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


def invert_tree(root: Node | None) -> Node | None:
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


def lca_binary_tree(root: Node | None, p: Node, q: Node) -> Node | None:
    if not root or root is p or root is q:
        return root
    left = lca_binary_tree(root.left, p, q)
    right = lca_binary_tree(root.right, p, q)
    if left and right:
        return root
    return left if left else right


def lca_bst(root: Node | None, p: Node, q: Node) -> Node | None:
    current = root
    while current:
        if p.val < current.val and q.val < current.val:
            current = current.left
        elif p.val > current.val and q.val > current.val:
            current = current.right
        else:
            return current
    return None


def tree_diameter(root: Node | None) -> int:
    diameter = 0

    def height(node: Node | None) -> int:
        nonlocal diameter
        if not node:
            return 0
        left = height(node.left)
        right = height(node.right)
        diameter = max(diameter, left + right)
        return 1 + max(left, right)

    height(root)
    return diameter


def is_balanced(root: Node | None) -> bool:
    def check(node: Node | None) -> int:
        if not node:
            return 0
        left = check(node.left)
        if left == -1:
            return -1
        right = check(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return check(root) != -1


def has_path_sum(root: Node | None, target_sum: int) -> bool:
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == target_sum
    return has_path_sum(root.left, target_sum - root.val) or has_path_sum(root.right, target_sum - root.val)


def max_path_sum(root: Node | None) -> int:
    best_sum = float("-inf")

    def dfs(node: Node | None) -> int:
        nonlocal best_sum
        if not node:
            return 0
        left = max(0, dfs(node.left))
        right = max(0, dfs(node.right))
        best_sum = max(best_sum, left + right + node.val)
        return node.val + max(left, right)

    dfs(root)
    return int(best_sum)


def is_valid_bst(root: Node | None, low: float = float("-inf"), high: float = float("inf")) -> bool:
    if not root:
        return True
    if not (low < root.val < high):
        return False
    return is_valid_bst(root.left, low, root.val) and is_valid_bst(root.right, root.val, high)


def kth_smallest_bst(root: Node | None, k: int) -> int:
    stack: list[Node] = []
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        k -= 1
        if k == 0:
            return current.val
        current = current.right
    raise ValueError("k is out of bounds")


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(3)
    root.right = Node(8)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right.left = Node(7)
    root.right.right = Node(9)

    assert dfs_inorder_rec(root) == [2, 3, 4, 5, 7, 8, 9]
    assert max_depth_rec(root) == 3
    assert tree_diameter(root) == 4
    assert is_valid_bst(root)
    assert kth_smallest_bst(root, 3) == 4
