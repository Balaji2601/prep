# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,val):
            if not node:
                return 0

            if node.val >= val:
                return 1+dfs(node.left,node.val)+dfs(node.right,node.val)
            else:
                return dfs(node.left,val)+dfs(node.right,val)
        
        return dfs(root,-float("inf"))