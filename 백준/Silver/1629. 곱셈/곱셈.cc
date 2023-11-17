#include <bits/stdc++.h>
using namespace std;

long long A, B, C;
long long f(long long A, long long B) {
	if (B == 1) return A % C;
	long long ret = f(A, B >> 1);
	ret = (ret * ret) % C;
	if (B & 1) ret = (ret * A) % C;
	return ret;
}

int main() {
	cin >> A >> B >> C;
	cout << f(A, B) << '\n';
	return 0;
}