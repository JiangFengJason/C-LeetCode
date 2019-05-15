using System;
using System.Collections.Generic;
using System.Text;

namespace Solutions
{
    class ReversMetrix
    {
        public void getReasult()
        {
            int[,] result=null;
            String lineNum = Console.ReadLine();
            int[,] metrix = new int[int.Parse(lineNum),int.Parse(lineNum)];
            for (int i = 0; i < int.Parse(lineNum); i++)
            {
                string inputStr = Console.ReadLine();
                string []inputList= inputStr.Split(' ');
                for (int j=0;j<int.Parse(lineNum);j++)
                {
                    metrix[i, j] = int.Parse(inputList[j]);
                }
            }
            int turn = int.Parse(Console.ReadLine());
            int choice = turn % 4;
            switch (choice)
            {
                case 0:
                    result = metrix;
                    break;
                case 1:
                    result = TurnOver(metrix, int.Parse(lineNum));
                    break;
                case 2:
                    result = TurnOver(metrix, int.Parse(lineNum));
                    result = TurnOver(result, int.Parse(lineNum));
                    break;
                case 3:
                    result = TurnOver(metrix, int.Parse(lineNum));
                    result = TurnOver(result, int.Parse(lineNum));
                    result = TurnOver(result, int.Parse(lineNum));
                    break;

            }
            for (int i=0;i<result.GetLength(0);i++)
            {
                for(int j=0;j<result.GetLength(1);j++)
                {
                    Console.Write(result[i, j]);
                    if (j != result.GetLength(0) + 1)
                        Console.Write(' ');
                }
                Console.WriteLine();
            }
        }
        public int [,] TurnOver(int[,] start,int linenum)
        {
            int[,] end = new int[linenum,linenum];
            for (int i = 0; i < linenum; i++)
            {
                for (int j = 0; j < linenum; j++)
                    end[j, linenum - 1 - i] = start[i, j];
            }
            return end;
        }
    }
}
