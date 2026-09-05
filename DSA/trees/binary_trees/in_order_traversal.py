# https://leetcode.com/problems/binary-tree-inorder-traversal/description/

from typing import List, Optional

# Inorder traversal is a depth-first tree traversal method that visits nodes 
# in the specific order of Left subtree, Root node, and Right subtree
# inorder -> [left_subtree, Root, right_subtree]
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node,path):
            if not node:
                return
            dfs(node.left,path)
            path.append(node.val)
            dfs(node.right,path)

            
        path = []
        dfs(root,path)
        return path