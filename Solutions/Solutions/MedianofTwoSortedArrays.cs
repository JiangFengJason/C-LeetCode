using System;
using System.Collections.Generic;
using System.Text;

namespace Solutions
{
    class MedianofTwoSortedArrays
    {
        public double FindMedianSortedArrays(int[] nums1, int[] nums2)
        {
            double res = 0;
            int nums1now = 0;
            int nums2now = 0;
            int now = 0;
            int next = 0;
            int counter = 0;
            int count = 0;
            int[] re = new int[3];
            if ((nums1.Length + nums2.Length) % 2 != 0)
                count = (nums1.Length + nums2.Length) / 2;
            else
                count = (nums1.Length + nums2.Length) / 2 - 1;

            if (nums1.Length == 0 && nums2.Length % 2 != 0)
                return nums2[count];
            else if (nums1.Length == 0 && nums2.Length % 2 == 0)
                return (nums2[count] + nums2[count + 1]) / 2.0;
            else if (nums2.Length == 0 && nums1.Length % 2 != 0)
                return nums1[count];
            else if (nums2.Length == 0 && nums1.Length % 2 == 0)
                return (nums1[count] + nums1[count + 1]) / 2.0;

            while (counter<=count)
            {
                re = check(nums1now, nums1, nums2now, nums2, now);
                now =re[0];
                nums1now = re[1];
                nums2now = re[2];
                counter++;
                
                if (counter== count+1)
                {
                    re=check(nums1now,nums1,nums2now,nums2,next);
                    next = re[0];
                    nums1now = re[1];
                    nums2now = re[2];
                }

            }
            if ((nums1.Length + nums2.Length) % 2 != 0)
                res = now;
            else
                res = (now + next) / 2.0;
            return res;
        }
        int[] check(int nums1now, int[] nums1, int nums2now,int[] nums2,int now)
        {
            if (nums1now < nums1.Length && nums2now < nums2.Length)
            {
                if (nums1[nums1now] <= nums2[nums2now])
                {
                    now = nums1[nums1now];
                    nums1now++;
                }
                else
                {
                    now = nums2[nums2now];
                    nums2now++;
                }
            }
            else if (nums1now == nums1.Length)
            {
                now = nums2[nums2now];
                nums2now++;
            }
            else if (nums2now == nums2.Length)
            {
                now = nums1[nums1now];
                nums1now++;
            }
            int[] re = new int[3];
            re[0] = now;
            re[1] = nums1now;
            re[2] = nums2now;
            return re;
        }
    }
}
