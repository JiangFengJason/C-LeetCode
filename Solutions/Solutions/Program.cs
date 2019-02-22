using System;

namespace Solutions
{
    class Program
    {
        static void Main(string[] args)
        {
            //TwoSum Solution1 = new TwoSum();
            //int[] test = new int[] { 2, 5, 7, 11 };
            //int target = 9;
            //int[] res = Solution1.ToTwoSum(test, target);
            //Console.WriteLine(res[0] + " " + res[1]);

            //AddTwoNumbers Solution2 = new AddTwoNumbers();
            //ListNode l1 = new ListNode(2);
            //l1.next = new ListNode(4);
            //l1.next.next = new ListNode(3);

            //ListNode l2 = new ListNode(5);
            //l2.next = new ListNode(6);
            //l2.next.next = new ListNode(4);

            //ListNode result = Solution2.ToAddTwoNumbers(l1, l2);

            //while(result!=null)
            //{
            //    Console.WriteLine(result.val);
            //    result = result.next;
            //}

            Reverse Solution3 = new Reverse();
            int origin =1534236469;
            Console.WriteLine(origin);
            int result = Solution3.toReverse(origin);
            Console.WriteLine(result);
        }
    }
}
