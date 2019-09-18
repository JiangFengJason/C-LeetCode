from RemoveDuplicatesfromSortedList import ListNode
class LinkedListII:
    def detectCycle(self, head):
        node=head
        visited=set()
        while node:
            if node in visited:
                return node
            else:
                visited.add(node)
                node=node.next
        return None