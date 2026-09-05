# https://leetcode.com/problems/binary-tree-postorder-traversal/description/

from typing import List, Optional

# Postorder traversal is a depth-first tree traversal method that visits nodes 
# in the exact order of Left subtree, Right subtree, and Root node
# post_order [left_subtree, right_subtree, Root]
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, path):
            if not node:
                return
            
            dfs(node.left, path)
            dfs(node.right, path)
            path.append(node.val)
        
        path = []
        dfs(root,path)
        return path