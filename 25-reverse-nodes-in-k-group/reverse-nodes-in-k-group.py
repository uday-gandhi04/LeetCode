# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        if k == 1 or not head:
            return head

        p=head
        count=1
        x=head
        pg=None
        pk=head
        while pk:
            grp_start=p
            while pk.next and count<k:
                pk=pk.next
                count+=1
            pkn=pk.next
            if count!=k:
                break
            
            count=1
            temp=p
            n=pk.next

            while p and p!=pkn:
                temp=p.next
                p.next=n
                n=p
                p=temp
            if x==head:
                head=n
            if pg:
                pg.next=n
            pg=grp_start
            p=pkn
            pk=pkn
            
        return head
