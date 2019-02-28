using System;
using System.Collections.Generic;
using System.Text;

namespace Solutions
{
    class LengthOfLongestSubstring
    {
        public int FindLengthOfLongestSubstring(string s)
        {
            int res = 0;
            List<char> character = new List<char>();
            for (int i=0;i<s.Length;i++)
            {
                if (!character.Contains(s[i]))
                {
                    character.Add(s[i]);
                }
                else
                {
                    res = Math.Max(res,character.Count);
                    i = i - character.Count+1;
                    character.Clear();
                    character.Add(s[i]);
                }
            }
            res = Math.Max(res, character.Count);
            return res;
        }
    }
}
