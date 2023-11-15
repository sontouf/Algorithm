#include <bits/stdc++.h>
using namespace std;

int arr[26];
string s, temp1;
int main() {
	cin >> s;
	int oddcnt = 0;
	int onlyodd = -1;
	for (char a : s) arr[a-'A']++;
	for (int i = 25; i >= 0; i--) {
		if (arr[i] & 1) {
			oddcnt++;
			if (oddcnt > 1) {
				cout << "I'm Sorry Hansoo" << '\n';
				exit(0);
			}
			onlyodd = i;
			arr[i]--;
		}
		for (int j = 0; j < arr[i]; j += 2) {
			temp1 = (char)(i + 'A') + temp1;
			temp1 += (char)(i + 'A');
		}
	}
	if (onlyodd != -1)
		temp1.insert(temp1.begin() + (temp1.size() / 2), onlyodd + 'A');
	cout << temp1 << '\n';

	return 0;
}