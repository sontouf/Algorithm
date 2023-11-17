#include <bits/stdc++.h>
using namespace std;

int n;

int main() {
	while (scanf("%d", &n) != EOF) {
		long long cnt = 1, ret = 1;
		while (1) {
			if (cnt % n  == 0) {
				printf("%lld\n", ret);
				break;
			}
			else {
				cnt = cnt * 10 + 1;
				cnt %= n;
				ret++;
			}
		}
	}
	return 0;
}