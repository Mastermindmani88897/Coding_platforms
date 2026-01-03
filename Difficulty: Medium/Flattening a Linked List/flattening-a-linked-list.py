class Solution:
    def flatten(self, root):
        if not root or not root.next:
            return root

        def merge(a, b):
            dummy = Node(0)
            curr = dummy
            while a and b:
                if a.data < b.data:
                    curr.bottom = a
                    a = a.bottom
                else:
                    curr.bottom = b
                    b = b.bottom
                curr = curr.bottom
                curr.next = None
            curr.bottom = a if a else b
            return dummy.bottom

        root.next = self.flatten(root.next)
        root = merge(root, root.next)
        return root
