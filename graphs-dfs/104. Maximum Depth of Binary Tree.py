### Question ###

"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Constraints:
# The number of nodes in the tree is in the range [0, 10^4]
# -100 <= Node.val <= 100
"""

### Algorithm ###

"""
Traversal depth of tree.

Base case: tree is empty.
Others: 
    the first layer is root, in this question, this layer has 1 depth.
    Use recursion:
    - traversal root.left
    - traversal root.right
    the bigger one is the depth of tree.
"""

### Complexity ###

"""
Time complexity:
    - right child: O(n/2)
    - left child: O(n/2)
    - root: O(1)
    That is 2 * O(n/2) + O(1) = O(n)

Space complexity:
    In the worst case is O(n)
"""

### Implementation ###


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    # "root.val == None" vs "not root"
    # "root.val == None" : heck for null value inside a node
    # "not root":  check for overall null node
    if not root: return 0

    left = maxDepth(root.left)
    right = maxDepth(root.right)
    
    return max(left, right) + 1


### Test ###

# root = [3,9,20,None,None,15,7], output = 3
# root = [1,None,2], output = 2
