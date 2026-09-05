# https://leetcode.com/problems/find-bottom-left-tree-value/description/


from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        ans = []
        while q:
            l = len(q)
            arr = []
            for i in range(l):
                node = q.popleft()
                arr.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(arr[0])
        
        return ans[-1]

# or
# check q[0] every time 
# because in while loop first element in q will be the extreme left node at each level in bfs.
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        ans = None
        while q:
            l = len(q)
            ans = q[0].val
            for i in range(l):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return ans
