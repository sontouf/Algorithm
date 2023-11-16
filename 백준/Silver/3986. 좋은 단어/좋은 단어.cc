#include <bits/stdc++.h>
using namespace std;

int N, cnt;
string s;
int main() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> s;
		stack<char> stk;
		for (int j = 0; j < s.size(); j++) {
			if (stk.size() && stk.top() == s[j]) stk.pop();
			else stk.push(s[j]);
		}
		if (stk.size() == 0) cnt++;
	}
	cout << cnt << '\n';
	return 0;
}