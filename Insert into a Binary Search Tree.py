# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        if root is None:
            return TreeNode(val)
        if val> root.val:
            root.right = self.insertIntoBST(root.right,val)
        else:
             root.left = self.insertIntoBST(root.left,val)
        return root
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        