using System;
using System.Collections.Generic;
using System.Text;

namespace Solutions
{
    class GenerateParentheses
    {
        public IList<string> GenerateParenthesis(int n)
        {
            IList<string> strlist = new List<string>();
            string str = "";
            search(strlist, str, 0, 0, n);
            return strlist;
        }
        void search(IList<string> strlist,string str,int start,int end,int max)
        {
            if (start+end==max*2)
            {
                strlist.Add(str);
                return;
            }
            if (start<max)
            {
                search(strlist, str + "(", start + 1, end, max);
            }
            if (end<start)
            {
                search(strlist, str + ")", start, end + 1, max);
            }
        }
    }
}
