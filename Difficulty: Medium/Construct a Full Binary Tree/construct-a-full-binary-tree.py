class Solution:
    def constructBinaryTree(self, pre, preMirror):
        pos = {v: i for i, v in enumerate(preMirror)}
        n = len(pre)
        preIndex = 0

        def build(l, r):
            nonlocal preIndex
            if preIndex >= n or l > r:
                return None

            root = Node(pre[preIndex])
            preIndex += 1

            if l == r or preIndex >= n:
                return root

            idx = pos[pre[preIndex]]

            if idx <= r:
                root.left = build(idx, r)
                root.right = build(l + 1, idx - 1)

            return root

        return build(0, n - 1)