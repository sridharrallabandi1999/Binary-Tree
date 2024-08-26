# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        bfs=[]
        left_to_right=True
        if root is None:
            return bfs
        queue = deque([])
        queue.append(root)
        while len(queue)!=0:
            level_size=len(queue)
            current_level=deque()
            for i in range(level_size):
                current=queue.popleft()

                if left_to_right:
                    current_level.append(current.val)
                else:
                    current_level.appendleft(current.val)

                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)

            bfs.append(current_level)
            left_to_right= not left_to_right
        return bfs 

        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        