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
            string str;
            Dictionary<string, bool> map = new Dictionary<string, bool>();
            for (int a = 0; a <= nums.Length - 3; a++)
            {
                int b = a + 1;
                int c = nums.Length - 1;
                while (b < c)
                {
                    if (nums[a] + nums[b] + nums[c] == 0)
                    {
                        str = nums[a].ToString() + nums[b].ToString() + nums[c].ToString();
                        if (map.ContainsKey(str))
                        {
                            b++;
                            c--;
                        }
                        else
                        {
                            IList<int> triplet = new List<int> { nums[a], nums[b], nums[c] };
                            map.Add(str, true);
                            result.Add(triplet);
                            b++;
                            c--;
                        }
                        
                    }
                    else if (nums[a] + nums[b] + nums[c] > 0)
                        c--;
                    else
                        b++;
                }
            }
            
             return result;
        }
    }
}
