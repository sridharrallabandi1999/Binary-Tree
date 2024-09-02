# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    diameter = 0
    def diameterOfBinaryTree(self, root):
        
        if root is None: return 0
        

        leftHeight = self.diameterOfBinaryTree(root.left)
        rightHeight = self.diameterOfBinaryTree(root.right)

        currentDiameter = leftHeight + rightHeight + 1

        self.diameter = max(currentDiameter, self.diameter)

        return max(leftHeight, rightHeight) + 1

        """
        :type root: TreeNode
        :rtype: int
        """
        