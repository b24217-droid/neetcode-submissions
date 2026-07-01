# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans  = True
        def dfs(p , q):
            nonlocal ans

            if not p and not q:
                return 0
            elif not p or not q:
                ans = False
                return 0

            else:
                if p.val != q.val:
                    ans  = False
    
            left = dfs(p.left , q.left)
            right = dfs(p.right , q.right)

            return 1 + max(left , right)

        dfs(p,q)
        return ans

