using System;

namespace Solutions
{
    class Program
    {
        static void Main(string[] args)
        {
            TwoSum Solution1 = new TwoSum();
            int[] test = new int[] { 2, 5, 7, 11 };
            int target = 9;
            int[] res = Solution1.toTwoSum(test, target);
            Console.WriteLine(res[0] + " " + res[1]);
        }
    }
}
