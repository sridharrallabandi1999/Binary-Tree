# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        bfs=[]
        if root is None:
            return bfs
        queue=deque([])
        queue.append(root)
        while len(queue)!=0:
            size=len(queue)
            current_level=[]

            for i in range(size):
                current=queue.popleft()
                current_level.append(current.val)

                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
            bfs.append(current_level)
        return bfs
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        