# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        if root is None:
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right,key)
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            cur = root.right
            while cur.left:
                cur=cur.left
            root.val =cur.val
            root.right = self.deleteNode(root.right,root.val)
                            
        return root


                
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        