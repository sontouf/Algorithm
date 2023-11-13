#include <bits/stdc++.h>
using namespace std;

int main()
{
	int arr[26] {0};
	string s;
	cin >> s;
	for (char i : s) {
		arr[(int)(i-'a')] += 1;
	}
	for (int i : arr) {
		cout << i << " ";
	}
	return 0;
}