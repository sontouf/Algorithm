#include <bits/stdc++.h>
using namespace std;

int main() {
	long long n = 0;
	cin >> n;
	long long cnt = 0;
	while (1) {
		if (n < 0) break;
		if (n % 5 == 0) break;
		n -= 3;
		cnt++;
	}
	if (n % 5 == 0) cout << n / 5 + cnt << '\n';
	else cout << -1 << '\n';
	return 0;
}