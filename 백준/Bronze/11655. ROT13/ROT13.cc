#include <bits/stdc++.h>
using namespace std;

string s;
int main() {
	getline(cin, s);
	for (int i = 0; i < s.size(); i++) {
		if (s[i] >= 'A' && s[i] <= 'Z') {
			s[i] = (s[i] -'A' + 13) % 26 + 'A';
		}
		else if (s[i] >= 'a' && s[i] <= 'z') {
			s[i] = (s[i] - 'a' + 13) % 26 + 'a';
		}
		cout << s[i];
	}
	cout << '\n';
	return 0;
}