# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        sett=set()

        p=headA

        while p:
            sett.add(p)
            p=p.next
        p=headB
        while p:
            if p in sett:
                return p
        
            p=p.next
        
        return None