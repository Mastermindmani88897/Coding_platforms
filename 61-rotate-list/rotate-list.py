class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        n = 1
        tail = head
        
        while tail.next:
            tail = tail.next
            n += 1
        
        k %= n
        if k == 0:
            return head
        
        tail.next = head
        
        steps = n - k
        curr = head
        
        for _ in range(steps - 1):
            curr = curr.next
        
        new_head = curr.next
        curr.next = None
        
        return new_head