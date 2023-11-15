#include <bits/stdc++.h>
using namespace std;

int arr[26];
string s, temp1, temp2;
int main() {
	cin >> s;
	int oddcnt = 0;
	int onlyodd = -1;
	for (int i = 0; i < s.size(); i++) {
		arr[s[i]- 'A']++;
	}
	for (int i = 0; i < 26; i++) {
		if (arr[i] % 2 == 1) {
			oddcnt++;
			if (oddcnt > 1) {
				cout << "I'm Sorry Hansoo" << '\n';
				exit(0);
			}
			onlyodd = i;
			for (int j = 0; j < (arr[i] - 1) / 2; j++) {
				temp1 += (char)(i + 'A');
			}
		}
		else {
			for (int j = 0; j < arr[i] / 2; j++) {
				temp1 += (char)(i + 'A');
			}
		}
	}
	temp2 = temp1;
	if (onlyodd != -1)
		temp2 += (char)(onlyodd + 'A');
	reverse(temp1.begin(), temp1.end());
	temp2 += temp1;
	cout << temp2 << '\n';

	return 0;
}