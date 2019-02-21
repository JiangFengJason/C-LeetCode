using System;
using System.Collections.Generic;
using System.Text;

namespace Solutions
{
    public class ListNode
    {
        public int val;
        public ListNode next;
        public ListNode(int x) { val = x; }
    }
    class AddTwoNumbers
    {
        public ListNode ToAddTwoNumbers(ListNode l1, ListNode l2)
        {
            return ToAdd(l1, l2, 0);
        }
        public ListNode ToAdd(ListNode l1, ListNode l2, int carry)
        {
            if (l1 == null && l2 == null && carry == 0) return null;

            int sum = 0;
            if (l1 != null)
                sum += l1.val;
            if (l2 != null)
                sum += l2.val;
            sum += carry;
            if (sum >= 10)
            {
                carry = 1;
                sum -= 10;
            }
            else
                carry = 0;

            ListNode result = new ListNode(sum);
            result.next = ToAdd(l1?.next, l2?.next, carry);
            return result;
        }
    }
}
