# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        result: List[List[int]] = []
        q: duque[Optional[TreeNode]] = deque()
        q.append(root)

        # loop while we have nodes to process
        while len(q) > 0:
            q_len:int = len(q)
            level: List[int] = []
            
            # loop over the len removing nodes and adding their children
            for _ in range(q_len):
                node: Optional[TreeNode] = q.popleft()
                if node is None:
                    continue
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
            if level:
                result.append(level)
        return result