# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def dfs(rl, rr):
            if not rl and not rr:
                return True
            if not rl or not rr:
                return False
            if rr.val != rl.val:
                return False
            return dfs(rl.left, rr.right) and dfs(rl.right, rr.left)
        return dfs(root.left, root.right)