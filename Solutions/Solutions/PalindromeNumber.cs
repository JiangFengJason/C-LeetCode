using System;
using System.Collections.Generic;
using System.Text;

namespace Solutions
{
    class PalindromeNumber
    {
        public bool IsPalindrome(int x)
        {
            int res = 0;
            int value = x;
            if (x < 0) return false;
            while (x!=0)
            {
                res = res * 10 + x % 10;
                x /= 10;
            }
            return value == res;
        }
    }
}
