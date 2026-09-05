# https://leetcode.com/problems/validate-binary-search-tree/description/

from typing import Optional

# Revise
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# brute force with path which carries in-order traversal of given binary tree
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, path):
            if not node:
                return
            dfs(node.left, path)
            path.append(node.val)
            dfs(node.right,path)
            
        path = []
        dfs(root, path)
        if path == sorted(path) and len(set(path)) == len(path):
            return True
        return False

# first I thought of doing this 
# managing root node condition is sufficient with right_val = float("inf") and left_val = -float("inf")
# but for this test case it failed
# [5,4,6,null,null,3,7]
# because for the root if we see right_subtree it is having 3 which is 3<5 but it should be 5<3 [not possible]
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return True
            right_val = float("inf")
            left_val = -float("inf")
            if node.left:
                left_val = node.left.val
            if node.right:
                right_val = node.right.val
            if left_val >= node.val or node.val >= right_val:
                return False
            if not dfs(node.left):
                return False
            if not dfs(node.right):
                return False
            return True
        
        return dfs(root)

# conclusion: we need to update left_val, right_val at each and every node 
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left_val, right_val):
            if not node:
                return True
            
            if not left_val < node.val < right_val:
                return False
            
            return dfs(node.left, left_val, node.val) and dfs(node.right, node.val, right_val)
        
        return dfs(root, -float("inf"), float("inf"))