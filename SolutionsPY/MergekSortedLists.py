class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class MergeKsorted(object):
    def mergeKLists(self, lists:ListNode):
        nodes=[]
        head=point=ListNode(0)
        for i in lists:
            while i:
                nodes.append(i.val)
                i=i.next
        for j in sorted(nodes):
            point.next=ListNode(j)
            point=point.next
        return head.next