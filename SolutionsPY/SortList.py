from RemoveDuplicatesfromSortedList import ListNode
class SortLi:
    def sortList(self, head: ListNode) -> ListNode:
        lis=[]
        while head:
            lis.append(head.val)
            head=head.next
        lis.sort()
        p=ListNode(0)
        s=p
        for i in range(len(lis)):
            p.next=ListNode(lis[i])
            p=p.next
        p.next=None
        return s.next
