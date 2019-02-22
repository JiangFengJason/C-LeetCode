#include <iostream>
#include "Reverse.h"
using namespace std;

int main()
{
	int origin = 123;
	int result = 0;
	Reverse re;
	result = re.reverse(origin);
	cout << result << endl;
	system("pause");
}
