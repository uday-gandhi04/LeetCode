# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        nums=set(nums)

        prev=None
        p=head
        p1=p.next

        while p1:
            if p.val in nums:
                if p==head:
                    head=p1
                    p=p1
                    p1=p1.next
                else:
                    p=p1
                    p1=p.next
                    prev.next=p
            else:
                prev=p
                p=p1
                p1=p1.next
        if p.val in nums:
            prev.next=None
            
        return head



        