using System;
using System.Collections.Generic;
using System.Text;

namespace Solutions
{
    class StringtoInteger
    {
        public int MyAtoi(string str)
        {
            int i = 0;
            int sign = 0;
            int val = 0;
            bool start = false;

            while (i < str.Length && ((str[i] >= '0' && str[i] <= '9') || str[i] == ' ' || str[i] == '-' || str[i] == '+'))
            {
                if ((val == 0 && sign == 0) && str[i] == ' '&&start==false)
                    i++;
                else if (str[i] == '-' && sign == 0 && start == false)
                {
                    sign = -1;
                    i++;
                }
                else if (str[i] == '+' && sign == 0 && start == false)
                {
                    sign = 1;
                    i++;
                }
                else if ((str[i] == '-' || str[i] == '+' || str[i] == ' ') &&start)
                {
                    break;
                }
                else if (str[i] >= '0' && str[i] <= '9')
                {
                    //handle overflow, val * 10 + n > int.MaxValue
                    if (val > (int.MaxValue - (str[i] - '0')) / 10)
                    {
                        if (sign == 0 || sign == 1)
                            return int.MaxValue;
                        return int.MinValue;
                    }
                    val = val * 10 + str[i] - '0';
                    start = true;
                    i++;
                }
                else
                {
                    if (sign == 0)
                        return val;
                    return val * sign;
                }
            }
            if (sign == 0)
                return val;
            return val * sign;
        }
    }
}
