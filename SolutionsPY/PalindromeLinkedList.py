# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True
        num=[head.val]
        slow=head
        quick=head
        while quick.next is not None and quick.next.next is not None:
            slow=slow.next
            num.append(slow.val)
            quick=quick.next.next
        if quick.next is None:
            num.pop()
        while slow.next is not None:
            slow=slow.next
            if slow.val==num[-1]:
                num.pop()
            else:
                return False
        return True