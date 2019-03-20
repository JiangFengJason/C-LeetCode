using System;
using System.Collections.Generic;
using System.Text;

namespace Solutions
{
    class LengthofLastWord
    {
        public int LengthOfLastWord(string s)
        {
            s = s.Trim();
            int lastIndex = s.LastIndexOf(' ') + 1;
            return s.Length - lastIndex;
        }
    }
}
