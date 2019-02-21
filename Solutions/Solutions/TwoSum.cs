using System;
using System.Collections.Generic;
using System.Text;

namespace Solutions
{
    class TwoSum
    {
        public int[] ToTwoSum(int [] nums,int target)
        {
            List<int[]> result = new List<int[]>();
            int[] aa = new int[2];
            for (int i = 0; i < nums.Length; i++)
            {
                for (int j = i + 1; j < nums.Length; j++)
                {
                    if (nums[i] + nums[j] == target && i != j)
                    {
                        aa[0] = i;
                        aa[1] = j;
                    }
                }
            }
            return aa;
        }
    }
}
