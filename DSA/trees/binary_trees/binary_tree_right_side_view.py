# https://leetcode.com/problems/binary-tree-right-side-view/description

from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
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
            ans.append(arr[-1])
        
        return ans

        