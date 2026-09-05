# https://leetcode.com/problems/delete-node-in-a-bst/description/


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insert(self, root: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, node2):
            if not node:
                return
            if node.val < node2.val:
                dfs(node.right,node2)
                if not node.right:
                    node.right = node2
            else:
                dfs(node.left,node2)
                if not node.left:
                    node.left = node2
        if not root2:
            return root
        dfs(root, root2)
        if not root:
            root = root2
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(node, r, branch):
            if not node:
                return
            if node.val < key:
                dfs(node.right, node, "r")
            elif node.val > key:
                dfs(node.left, node, "l")
            else:
                right_subtree = node.right
                left_subtree = node.left
                if branch == "r":
                    if not right_subtree:
                        r.right = left_subtree
                    else:
                        right_subtree = self.insert(right_subtree, left_subtree)
                        r.right = right_subtree
                else:
                    if not right_subtree:
                        r.left = left_subtree
                    else:
                        right_subtree = self.insert(right_subtree, left_subtree)
                        r.left = right_subtree
        if not root:
            return root
        if root.val == key:
            left_subtree = root.left
            right_subtree = root.right
            if not right_subtree:
                return left_subtree
            else:
                right_subtree = self.insert(right_subtree, left_subtree)
                return right_subtree
        dfs(root, None, "")
        return root