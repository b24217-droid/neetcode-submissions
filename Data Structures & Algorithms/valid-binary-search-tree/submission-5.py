# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # see i want for any given tree the root val should be lesser than the minimum value present in the right part
        # and should be greater than the maximum value present at the left most part
        ans = True
        def dfs(root): # return the mini and maxi value in the current tree
            nonlocal ans
            if not root:
                return float('inf') , float('-inf')

            left = dfs(root.left)
            right = dfs(root.right)
            if root.val >= right[0] or root.val <= left[1]:
                ans = False

            mini , maxi = left[0] , right[1]
            if root.val < mini:
                mini = root.val
            if root.val > maxi:
                maxi = root.val

            return mini , maxi
        dfs(root)
        return ans
        
