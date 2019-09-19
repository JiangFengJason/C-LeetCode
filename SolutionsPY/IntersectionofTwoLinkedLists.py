from RemoveDuplicatesfromSortedList import ListNode
class IntersectionofTwoLinked:
    def getIntersectionNode(self, headA, headB):
        ha=headA
        hb=headB
        while ha!=hb:
            ha=ha.next if ha else headB
            hb=hb.next if hb else headA
        return ha