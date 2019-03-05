using System;
using System.Collections.Generic;
using System.Text;

namespace Solutions
{
    class ImplementStr
    {
        public int StrStr(string haystack, string needle)
        {
            
            if (needle.Length == 0)
                return 0;
            if (haystack.Length == 0)
                return -1;
            if (needle.Length > haystack.Length)
                    return -1;
           
            for (int i = 0; i < haystack.Length; i++)
            {
                if (haystack[i]==needle[0])
                {
                    bool found = true;
                    for (int j = 0; j < needle.Length; j++)
                    {
                        if ((i+j)>=haystack.Length||haystack[i + j] != needle[j])
                        {
                            found = false;
                            break;
                        }
                    }
                    if (found)
                        return i;
                }
            }
            
            return -1;
        }
    }
}
