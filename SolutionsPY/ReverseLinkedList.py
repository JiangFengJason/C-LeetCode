from RemoveDuplicatesfromSortedList import ListNode
class ReverseLinkedLi:
    def reverseList(self, head):
        start= ListNode(0)
        while head:
            tmp=ListNode(head.val)
            tmp.next=start.next
            start.next=tmp
            head=head.next
        return start.next