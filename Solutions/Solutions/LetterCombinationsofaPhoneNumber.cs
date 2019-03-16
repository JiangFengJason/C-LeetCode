using System;
using System.Collections.Generic;
using System.Text;

namespace Solutions
{
    class LetterCombinationsofaPhoneNumber
    {
        public IList<string> LetterCombinations(string digits)
        {
            IList<string> res = new List<string>();
            if (digits.Length==0) return res;
            string[] dict = { "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" };
            letterCombinationsDFS(digits, dict, 0, "", res);
            return res;
        }

        void letterCombinationsDFS(string digits, string[] dict, int level, string output, IList<string> res)
        {
            if (level == digits.Length)
            {
                res.Add(output);
                return;
            }
            string str = dict[digits[level] - '0'];
            for (int i = 0; i < str.Length; ++i)
            {
                letterCombinationsDFS(digits, dict, level + 1, output +str[i], res);
            }
        }
    }
    }
}
