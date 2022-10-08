# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/delete-node-in-a-bst/

class Solution:
    def PredecessorSuccessor(self, root: TreeNode, flag) -> int:
            # successor: min value in right subtree
            if flag == 0:
                root = root.right
                while root.left:
                    root = root.left
                return root.val
            # predecessor: max value in lefr subtree
            if flag == 1:
                root = root.left
                while root.right:
                    root = root.right
                return root.val
        
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # leafnode
            if not (root.left or root.right):
                root = None
            # nonleaf node with right child only
            elif root.right:
                # find predecessor to swap out with deleted right node
                root = self.PredecessorSuccessor(root, 0)
                root.right = self.deleteNode(root.right, root.val)
            # nonleaf node with left child   
            elif root.left:
                # find successor to swap out with deleted left node
                root.val = self.PredecessorSuccessor(root, 1)
                root.left = self.deleteNode(root.left, root.val)
                        
        return root
