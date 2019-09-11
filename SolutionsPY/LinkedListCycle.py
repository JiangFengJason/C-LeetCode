from RemoveDuplicatesfromSortedList import ListNode
class LinkedList:
    def hasCycle(self, head):
        if head==None or head.next==None:
            return False
        slow=head
        fast=head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow=slow.next
            fast=fast.next.next
        return True