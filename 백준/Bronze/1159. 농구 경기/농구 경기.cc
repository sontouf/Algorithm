#include <bits/stdc++.h>
using namespace std;

int alpha[26];
int n, cnt;
string player, ret;
int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> player;
		alpha[player[0] - 'a'] += 1;
		if (alpha[player[0] - 'a'] >= 5) cnt = 1;
	}
	if (cnt == 0) {
		cout << "PREDAJA" << '\n';
	}
	else {
		for (int i = 0; i < 26; i++) {
			if (alpha[i] >= 5)
				cout << (char)(i + 'a');
		}
		cout << '\n';
	}
	return 0;
}