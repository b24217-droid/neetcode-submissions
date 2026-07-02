# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def rec(p , q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            if p.val == q.val:
                return rec(p.left , q.left) and rec(p.right , q.right)
            else:
                return False

        return rec(p,q)