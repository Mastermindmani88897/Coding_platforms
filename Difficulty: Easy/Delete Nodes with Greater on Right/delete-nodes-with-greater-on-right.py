class Solution:
    def compute(self, head):
        
        def reverse(node):
            prev = None
            curr = node
            
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            return prev
        
        head = reverse(head)
        
        max_so_far = head.data
        curr = head
        
        while curr and curr.next:
            if curr.next.data < max_so_far:
                curr.next = curr.next.next
            else:
                curr = curr.next
                max_so_far = curr.data
        
        return reverse(head)