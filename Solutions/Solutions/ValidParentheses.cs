using System;
using System.Collections.Generic;
using System.Text;

namespace Solutions
{
    class ValidParentheses
    {
        public bool IsValid(string s)
        {
            if (s.Length % 2 != 0)
                return false;
            Stack<char> stack = new Stack<char>();
            for (int i=0;i<s.Length;i++)
            {
                if (s[i] == '(')
                {
                    stack.Push('(');
                }
                else if (s[i] == '[')
                {
                    stack.Push('[');
                }
                else if (s[i] == '{')
                {
                    stack.Push('{');
                }
                else if (s[i] == ')')
                {
                    if (stack.Count==0|| stack.Peek() != '(')
                        return false;
                    else
                        stack.Pop();
                }
                else if (s[i] == ']')
                {
                    if ( stack.Count == 0|| stack.Peek() != '[')
                        return false;
                    else
                        stack.Pop();
                }
                else if (s[i] == '}')
                {
                    if ( stack.Count == 0|| stack.Peek() != '{')
                        return false;
                    else
                        stack.Pop();
                }
            }
            return stack.Count==0;
        }
    }
}
