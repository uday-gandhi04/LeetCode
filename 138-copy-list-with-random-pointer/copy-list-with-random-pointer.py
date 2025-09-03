"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        
        dic={}

        p=head
        n=Node(p.val)
        p1=p.next
        dic[p]=n
        while p1!=None:
            n=Node(p1.val)
            dic[p].next=n
            dic[p1]=n

            p=p1
            p1=p1.next
        
        p=head
        while p:
            if not p.random:
                p=p.next
                continue
            dic[p].random=dic[p.random]
            p=p.next

        return dic[head]
        