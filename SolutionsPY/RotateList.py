from RemoveDuplicatesfromSortedList import ListNode
class RotateL:
    def rotateRight(self, head, k):
        if head == None:
            return head
        if k == 0:
            return head
        
        point=ListNode(0)
        point.next=head
        p=point
        count=0
        while p.next:
            p=p.next
            count+=1
        p.next=head
        step=count-(k%count)
        for i in range(step):
            p=p.next
        head=p.next
        p.next=None
        return head