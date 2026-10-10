# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter is left + right
        # height is 1 + max(left) + max(right)
        self.diam = 0 # NEED TO ADD SELF TO MAKE IT ACCESIBLE

        # returning height
        def dfs(rt):
            if not rt:
                return 0
            left = dfs(rt.left)
            right = dfs(rt.right)
            self.diam = max(self.diam, left+right) # diameter
            return 1 + max(left, right) # height
        
        dfs(root)
        return self.diam
