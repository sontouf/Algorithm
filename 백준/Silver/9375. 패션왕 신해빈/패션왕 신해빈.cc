#include <bits/stdc++.h>
using namespace std;

int T, N;
string a, b;
int main() {
	cin >> T;
	while (T--) {
		map<string, int> mapping;
		cin >> N;
		for (int i = 0; i < N; i++) {
			cin >> a >> b;
			mapping[b]++;
		}
		long long ret = 1;
		for (auto c : mapping) {
			ret *= ((long long)c.second + 1);
		}
		ret--;
		cout << ret << '\n';
	}
	return 0;
}