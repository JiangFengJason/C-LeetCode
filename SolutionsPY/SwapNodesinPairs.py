class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Swap:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        else:
            start=ListNode(0)
            start.next=head
            p=start
            q=start.next
            while q!=None and q.next!=None:
                p.next=q.next
                q.next=p.next.next
                p.next.next=q
                p=q
                q=q.next
            return start.next

        