# https://leetcode.com/problems/binary-tree-preorder-traversal/description/

from typing import List, Optional

# Preorder traversal is a depth-first tree traversal method that visits nodes
# in the exact order of Root, then Left Subtree, and finally Right Subtree.
# preorder: [Root, left_subtree, right_subtree]
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node: Optional[TreeNode], path: List[int]):
            if not node:
                return
            
            path.append(node.val)
            dfs(node.left, path)
            dfs(node.right, path)

        path = []
        dfs(root, path)
        return path