# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        cur,stack=root,[]
        res=[]
        while cur or stack :
            if cur:
                res.append(cur.val)
                stack.append(cur.right)
                cur=cur.left
            else:
                cur=stack.pop()
        return res

        """
        :type root: TreeNode
        :rtype: List[int]
        """
        