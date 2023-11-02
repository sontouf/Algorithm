#include <iostream>
#include <iomanip>
using namespace std;

int max_width;

int printvalue(int i, int j)
{
	if (i == j && i >= 0)
		return (2*i + 1)*(2*i + 1);
	if (j > 0 && j - 1 >= i && i>= -j)
		return (j*2-1)*(j*2-1) + j - i;
	if (i < 0 && -(1+i) >= j && j >= i)
		return 2*i*(2*i + 1) + 1 - (j + i);
	if (j < 0 && -j >= i && i >= 1+j)
		return (j*2+1)*(j*2+1) - 5*j + i;
	if (i > 0 && i >= j && j>= 1-i)
		return (i*2-1)*(i*2-1) + 7*i + j;
	else
		return 0;
}
	
pair<int, int> width(int i, int j)
{
	int result = printvalue(i, j);
	int temp = result;
	int count = 0;
	while (temp)
	{
		count += 1;
		temp = temp / 10;
	}
	return pair(count, result);
}


void whitespace(int i, int j)
{
	pair<int, int> value = width(i, j);
	int cur_width = value.first;
	int result = value.second;
	int temp = max_width - cur_width;
	cout << setw(max_width) << result;
}

int main(void)
{
	max_width = 0;
	int r1, c1, r2, c2;
	cin >> r1 >> c1 >> r2 >> c2;
	for (int i = r1; i <= r2; i++)
	{
		for (int j = c1; j <= c2; j++)
		{
			pair<int, int> value = width(i, j);
			int cur_width = value.first;
			int temp = value.second;			
			max_width = max(max_width, cur_width);
		}
	}

	for (int i = r1; i < r2; i++)
	{
		for (int j = c1; j < c2; j++)
		{
			whitespace(i, j);
			cout << ' ';
		}
		whitespace(i ,c2);
		cout << '\n';
	}
	for (int j = c1; j < c2; j++)
	{
		whitespace(r2, j);
		cout << ' ';
	}
	whitespace(r2, c2);
}