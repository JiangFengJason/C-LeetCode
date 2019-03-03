using System;
using System.Collections.Generic;
using System.Text;

namespace Solutions
{
    class RemoveDuplicatesfromSortedArray
    {
        public int RemoveDuplicates(int[] nums)
        {
            int num = 0;
            int i;
            for (i = 0; i < nums.Length; i++)
            {
                while (i > 0 && i < nums.Length && nums[i] == nums[i - 1]) i++;
                if (i < nums.Length)
                {
                    nums[num++] = nums[i];
                }
            }
            return num;
        }
    }
}
