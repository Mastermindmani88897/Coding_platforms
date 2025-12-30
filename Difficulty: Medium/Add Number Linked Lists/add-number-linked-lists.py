class Solution:
    def addTwoLists(self, head1, head2):
        s1, s2 = [], []

        while head1:
            s1.append(head1.data)
            head1 = head1.next

        while head2:
            s2.append(head2.data)
            head2 = head2.next

        carry = 0
        head = None

        while s1 or s2 or carry:
            x = s1.pop() if s1 else 0
            y = s2.pop() if s2 else 0

            total = x + y + carry
            carry = total // 10

            node = Node(total % 10)
            node.next = head
            head = node

        while head and head.data == 0 and head.next:
            head = head.next

        return head
