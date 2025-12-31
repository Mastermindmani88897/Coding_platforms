'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def isPalindrome(self, head):
        # code here
        currNode=head
        s=[]
        while currNode is not None:
            s.append(currNode.data)
            currNode=currNode.next
        while head is not None:
            c=s.pop()
            if head.data!=c:
                return False
            head=head.next
        return True
            
        
        
        