from RemoveDuplicatesfromSortedList import ListNode
class DeletNodeinaLinked:
    def deleteNode(self, node):
        node.val=node.next.val
        node.next=node.next.next