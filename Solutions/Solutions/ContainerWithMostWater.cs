using System;
using System.Collections.Generic;
using System.Text;

namespace Solutions
{
    class ContainerWithMostWater
    {
        public int MaxArea(int[] height)
        {
            int water = 0;
            for (int i=0;i<height.Length;i++)
            {
                for (int j=i+1;j<height.Length;j++)
                {
                    water = Math.Max((j - i) * Math.Min(height[i], height[j]), water);
                }
            }
            return water;
        }
    }
}
