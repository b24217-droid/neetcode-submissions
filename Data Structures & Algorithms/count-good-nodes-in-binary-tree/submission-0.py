# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root , max_encountered):
            nonlocal res
            if not root:
                return 0

            if root.val >= max_encountered:
                max_encountered = root.val
                res += 1
            
            
            left = dfs(root.left,max_encountered)
            right = dfs(root.right ,max_encountered)

            return 1 + max(left , right)

        dfs(root , float('-inf'))

        return res
