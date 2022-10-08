# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

# Example 1:

# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

# Example 2:

# Input: root = [1,2]
# Output: 1




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]):
        if not root:
            return 0
        diam = 0
        
        def maxDepth(root: Optional[TreeNode]):
            nonlocal diam
            if not root:
                return 0
            # get depth of left and right subtrees
            ltree = maxDepth(root.left)
            rtree = maxDepth(root.right)
            
            # diam would be sum of max depth on left and max depth on right
            diam = max(diam, ltree+rtree)
            
            # return depth since we still need to calc that. Diam passed in by reference using nonlocal
            return 1 + max(ltree, rtree)
        
        maxDepth(root)
        return diam
