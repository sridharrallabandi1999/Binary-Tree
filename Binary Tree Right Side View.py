# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        result = []
        if root is None:
            return result
        queue=deque([])
        queue.append(root)
        while len(queue)!=0:
            size=len(queue)
            for i in range(size):
                current = queue.popleft()
                if(i == size-1):
                    result.append(current.val)

                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)

        return result
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        