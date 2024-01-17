
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # DEPTH FS
        # find leaf value of root 1
        # fine leaf value of root 2

        def DFS(root):
            if not root: return []
            if not root.left and not root.right: return [root.val]

            return DFS(root.left) + DFS(root.right)

        # return if they are the same
        return DFS(root1) == DFS(root2)