# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return
            if node.val < val:
                dfs(node.right)
                if not node.right:
                    node.right = TreeNode(val)
            else:
                dfs(node.left)
                if not node.left:
                    node.left = TreeNode(val)
        dfs(root)
        if not root:
            root = TreeNode(val)
        return root