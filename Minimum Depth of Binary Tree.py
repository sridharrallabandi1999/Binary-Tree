# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        min_depth=0
        if root is None:
            return min_depth
        queue=deque([])
        queue.append(root)
        while len(queue)!=0:
            min_depth+=1
            size=len(queue)
            for i in range(size):
                current=queue.popleft()
                if current.left is None and current.right is None:
                    return min_depth
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)

        return min_depth


        """
        :type root: TreeNode
        :rtype: int
        """
        