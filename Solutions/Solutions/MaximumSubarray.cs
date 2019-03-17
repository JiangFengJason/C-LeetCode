using System;
using System.Collections.Generic;
using System.Text;

namespace Solutions
{
    class MaximumSubarray
    {
        public int MaxSubArray(int[] nums)
        {
            int sum = 0;
            int ans;
            ans = nums[0];
            for (int i = 0; i < nums.Length; i++)
            {
                sum += nums[i];
                ans = Math.Max(ans, sum);
                sum = Math.Max(sum, 0);
            }
            return ans;
        }
    }
}
