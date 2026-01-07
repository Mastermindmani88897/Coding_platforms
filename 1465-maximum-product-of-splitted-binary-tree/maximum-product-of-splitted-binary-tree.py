# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root):
        MOD=1000000007
        subs=[]
        
        def dfs(node):
            if not node:
                return 0
            s=node.val+dfs(node.left)+dfs(node.right)
            subs.append(s)
            return s
        
        total=dfs(root)
        ans=0
        for s in subs:
            ans=max(ans,s*(total-s))
        return ans%MOD
