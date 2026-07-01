# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')

        def dfs(root):
            nonlocal ans
            if not root.left and not root.right:
                ans = max(ans , root.val)
                return root.val

            left = max( 0 , dfs(root.left) if root.left else 0)
            right = max( 0 , dfs(root.right) if root.right else 0)

            ans = max(ans , left + right + root.val)
            return root.val + max(left , right)

        dfs(root)
        return ans
