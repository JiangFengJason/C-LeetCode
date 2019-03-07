using System;
using System.Collections.Generic;
using System.Text;

namespace Solutions
{
    class SearchInsertPosition
    {
        public int SearchInsert(int[] nums, int target)
        {
            int i = 0;
            for (i=0;i<nums.Length;i++)
            {
                if (nums[i] == target)
                    return i;
                else if (nums[i] > target)
                    return i;
            }
            if (nums.Length==0)
                return 0;
            else
                return i;
        }
    }
}
