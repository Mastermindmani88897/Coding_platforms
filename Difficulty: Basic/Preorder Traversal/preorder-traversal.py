class Solution:
    def preOrder(self, root):
        ans = []

        def dfs(node):
            if not node:
                return
            ans.append(node.data)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ans