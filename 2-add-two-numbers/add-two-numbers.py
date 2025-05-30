# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry =0
        head=None
        p=head
        p1=l1
        p2=l2

        while p1!=None and p2!=None:
            temp=ListNode()
            summ=p1.val+p2.val+carry

            if summ>9:
                carry=1
            else:
                carry=0
            
            temp.val = summ%10

            if head==None:
                head=temp
                p=head
            else:
                p.next=temp
                p=p.next
            
            p1=p1.next
            p2=p2.next

        while p1!=None:
            temp=ListNode()
            summ=p1.val+carry

            if summ>9:
                carry=1
            else:
                carry=0
            
            temp.val = summ%10

            if head==None:
                head=temp
                p=head
            else:
                p.next=temp
                p=p.next
            p1=p1.next
        
        while p2!=None:
            temp=ListNode()
            summ=p2.val+carry

            if summ>9:
                carry=1
            else:
                carry=0
            
            temp.val = summ%10

            if head==None:
                head=temp
                p=head
            else:
                p.next=temp
                p=p.next
            p2=p2.next
        
        if carry==1:
            temp=ListNode(1,None)
            p.next=temp
            carry=0
        
        return head