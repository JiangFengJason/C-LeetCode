using System;
using System.Collections.Generic;
using System.Text;

namespace Solutions
{
    class RemoveNthNodeFromEndofList
    {
        public ListNode RemoveNthFromEnd(ListNode head, int n)
        {
            ListNode p = head;
            ListNode q = head;
            if (head.next==null) return null;
            for (int i = 0; i < n; ++i) q = q.next;
            if (q==null) return head.next;
            while (q.next!=null)
            {
                q = q.next;
                p = p.next;
            }
            p.next = p.next.next;
            return head;
        }
    }
}
