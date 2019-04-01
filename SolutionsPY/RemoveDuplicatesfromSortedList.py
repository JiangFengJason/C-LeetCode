class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class Remove:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p=head
        while p:
            if p.next and p.next.val==p.val:
                p.next=p.next.next
            else :
                p=p.next
        return head