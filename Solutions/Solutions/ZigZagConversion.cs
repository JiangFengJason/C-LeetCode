using System;
using System.Collections.Generic;
using System.Text;

namespace Solutions
{
    class ZigZagConversion
    {
        public string Convert(string s, int numRows)
        {
            int column = 0;
            if (numRows==1||s.Length==1||s.Length==0|| numRows == 0|| numRows>=s.Length)
                return s;
            if (s.Length % (numRows + numRows - 2) == 0)
                column = s.Length / (numRows + numRows - 2) * (numRows - 1);
            else
                column = (s.Length / (numRows + numRows - 2)+1) * (numRows - 1);
            char[,] origin = new char[numRows,column];
            for (int i = 0; i < numRows; i++)
            {
                for (int j = 0; j < column; j++)
                {
                    origin[i, j]=' ';
                }
            }
            
            int counter = 0;
            for (int i = 0; i < column; i++)
            {
                for (int j = 0; j < numRows; j++)
                {
                    if ((i % (numRows-1) == 0)&&counter<s.Length)
                    {
                        origin[j, i] = s[counter];
                        counter++;
                    }
                    else if ((j == (numRows-1 - i % (numRows-1)))&& counter < s.Length)
                    {
                        origin[j, i] = s[counter];
                        counter++;
                    }
                }
            }
            char[] finalstring = new char[s.Length];
            counter = 0;
            for (int i = 0; i < numRows; i++)
            {
                for (int j = 0; j < column; j++)
                {
                    if (origin[i, j] != ' '&&counter<s.Length)
                    {
                        finalstring[counter] = origin[i, j];
                        counter++;
                    }
                        
                }
            }
            string final=new string(finalstring);
            return final;
        }
    }
}
