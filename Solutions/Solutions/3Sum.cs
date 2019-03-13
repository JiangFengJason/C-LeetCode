using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Solutions
{
    class _3Sum
    {
        public IList<IList<int>> ThreeSum(int[] nums)
        {
            Array.Sort(nums);
            IList<IList<int>> result = new List<IList<int>>();
            if (nums.Length <= 2)
                return result;
            int m;
            for(m=0;m<nums.Length;m++)
            {
                if (nums[m] != 0)
                    break;
            }
            if (m==nums.Length)
            {
                IList<int> success = new List<int>();
                success.Add(0);
                success.Add(0);
                success.Add(0);
                result.Add(success);
                return result;
            }
            for (int i = 0; i < nums.Length; i++)
            {
                for (int j = i + 1; j < nums.Length; j++)
                {
                    for (int k = j + 1; k < nums.Length; k++)
                    {
                        if (nums[i] + nums[j] + nums[k] == 0)
                        {
                            IList<int> success = new List<int>();
                            success.Add(nums[i]);
                            success.Add(nums[j]);
                            success.Add(nums[k]);
                            result.Add(success);
                            break;
                        }
                    }
                }
            }
            for(int l=0;l<result.Count;l++)
            {
                for (int o=1;o< result.Count;o++)
                {
                    if (result[l].All(result[o].Contains) && result[l].Count == result[o].Count)
                        result.Remove(result[o]);
                }
            }
            return result;
        }
    }
}
