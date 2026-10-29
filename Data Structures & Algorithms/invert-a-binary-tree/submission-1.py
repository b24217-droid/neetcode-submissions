# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # to do by recursion hmm 

        if not root or ( not root.left and not root.right):
            return root

        l = self.invertTree(root.left)
        r = self.invertTree(root.right)

        root.left = r
        root.right = l 

        return root 
        
