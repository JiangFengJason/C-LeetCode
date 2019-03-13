using System;
using System.Collections.Generic;

namespace Solutions
{
    public class ListNode
    {
        public int val;
        public ListNode next;
        public ListNode(int x) { val = x; }
    }
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

            //Reverse Solution3 = new Reverse();
            //int origin =1534236469;
            //Console.WriteLine(origin);
            //int result = Solution3.toReverse(origin);
            //Console.WriteLine(result);

            //int number = 121;
            //bool result = false;
            //PalindromeNumber pn = new PalindromeNumber();
            //result = pn.IsPalindrome(number);
            //Console.WriteLine(result);

            //string Roman = "MCMXCIV";
            //int num;
            //RomantoInt rom = new RomantoInt();
            //num = rom.RomanToInt(Roman);
            //Console.WriteLine(num);

            //string[] objects = { "aa", "a" };
            //string result;
            //LongestCommonPre pre = new LongestCommonPre();
            //result = pre.LongestCommonPrefix(objects);
            //Console.WriteLine(result);

            //string str = "{{";
            //bool result = false;
            //ValidParentheses vp = new ValidParentheses();
            //result = vp.IsValid(str);
            //Console.WriteLine(result);

            //string str = "aab";
            //int res = 0;
            //LengthOfLongestSubstring lls = new LengthOfLongestSubstring();
            //res = lls.FindLengthOfLongestSubstring(str);
            //Console.WriteLine(res);

            //MergeTwoSortedLists merge = new MergeTwoSortedLists();
            //ListNode l1 = new ListNode(1);
            //l1.next = new ListNode(2);
            //l1.next.next = new ListNode(4);

            //ListNode l2 = new ListNode(3);
            //l2.next = new ListNode(5);
            //l2.next.next = new ListNode(6);

            //ListNode result = merge.MergeTwoLists(l1, l2);
            //while (result != null)
            //{
            //    Console.WriteLine(result.val);
            //    result = result.next;
            //}

            //RemoveDuplicatesfromSortedArray tore = new RemoveDuplicatesfromSortedArray();
            //int[] nums = { 1, 1, 1, 2 };
            //int num = tore.RemoveDuplicates(nums);
            //Console.WriteLine(num);

            //RemoveElement tore = new RemoveElement();
            //int[] nums = { 0,1,2,2,3,0,4,2};
            //int val = 2;
            //int res = tore.toRemoveElement(nums, val);
            //    Console.WriteLine(res);

            //ImplementStr imp = new ImplementStr();
            //string haystack = "hello";
            //string needle = "ll";
            //int res = imp.StrStr(haystack, needle);
            //Console.WriteLine(res);

            //ZigZagConversion zig = new ZigZagConversion();
            //string ori = "ABCD";
            //int num = 3;
            //string res = zig.Convert(ori, num);
            //Console.WriteLine(res);

            //SearchInsertPosition sea = new SearchInsertPosition();
            //int[] nums = { 1, 3, 5, 6 };
            //int target = 7;
            //int res = sea.SearchInsert(nums, target);
            //Console.WriteLine(res);

            //StringtoInteger sti = new StringtoInteger();
            //string str = "0-1";
            //int res = sti.MyAtoi(str);
            //Console.WriteLine(res);

            //CountandSay cas = new CountandSay();
            //int count = 4;
            //string res = cas.toCountAndSay(count);
            //Console.WriteLine(res);

            //ContainerWithMostWater wat = new ContainerWithMostWater();
            //int[] height = { 1, 8, 6, 2, 5, 4, 8, 3, 7 };
            //int water = wat.MaxArea(height);
            //Console.WriteLine(water);

            _3Sum s = new _3Sum();
            int[] num = { -1, 0, 1, 2, -1, -4 };
            IList<IList<int>> res = s.ThreeSum(num);
            
        }
    }
}
