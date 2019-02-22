using System;
using System.Collections.Generic;
using System.Text;

namespace Solutions
{
    class Reverse
    {
        public int toReverse(int x)
        {
            int res = 0;
            while (x != 0)
            {
                int t = res * 10 + x % 10;
                if ((t - x % 10) / 10 != res) return 0;
                res = t;
                x /= 10;
            }
            return res;
        }
    }
}
