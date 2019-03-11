using System;
using System.Collections.Generic;
using System.Text;

namespace Solutions
{
    class CountandSay
    {
        public string toCountAndSay(int n)
        {
            if (n <= 0) return "";
            string res = "1";
            while (--n != 0)
            {
                string cur = "";
                for (int i = 0; i < res.Length; ++i)
                {
                    int cnt = 1;
                    while (i + 1 < res.Length && res[i] == res[i + 1])
                    {
                        ++cnt;
                        ++i;
                    }
                    cur += cnt.ToString() + res[i];
                }
                res = cur;
            }
            return res;
        }
    }
}
