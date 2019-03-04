using System;
using System.Collections.Generic;
using System.Text;

namespace Solutions
{
    class RemoveElement
    {
        public int toRemoveElement(int[] nums, int val)
        {
            int res = 0;
            int j = nums.Length - 1;
            for (int i=0;i<j+1;i++)
            {
                if (nums[i] == val)
                {
                    res++;
                    for (;j>i;j--)
                    {
                        if (nums[j] != val)
                        {
                            nums[i] = nums[j];
                            j--;
                            break;
                        }
                        else
                            res++;
                    }
                }
            }
            return nums.Length - res;
        }
    }
}
