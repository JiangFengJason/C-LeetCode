using System;
using System.Collections.Generic;
using System.Text;

namespace Solutions
{
    class RomantoInt
    {
        private static Dictionary<char, int> dic = new Dictionary<char, int>
        {
            {'I',1},
            {'V',5},
            {'X',10},
            {'L',50},
            {'C',100},
            {'D',500},
            {'M',1000},
        };

        public int RomanToInt(string s)
        {
            int res = 0;
            for (int i=0;i<s.Length;i++)
            {
                if (i==s.Length-1||dic[s[i]]>=dic[s[i+1]])
                {
                    res += dic[s[i]];
                }
                else
                {
                    res -= dic[s[i]];
                }
            }
            return res;
        }

    }
}
