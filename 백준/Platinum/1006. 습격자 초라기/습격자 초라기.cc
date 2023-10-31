#include<bits/stdc++.h>

int N, W;
int firstfloor[10000], secondfloor[10000];
int a[10001], b[10001], c[10001];
using namespace std;

void attack(int start)
{
	for (int i = start; i < N; i++) {
		a[i+1] = min(b[i], c[i]) + 1;
		if (firstfloor[i] + secondfloor[i] <= W)
			a[i+1] = min(a[i+1], a[i] + 1);
		if (i > 0 && firstfloor[i-1] + firstfloor[i] <= W && secondfloor[i-1] + secondfloor[i] <= W)
			a[i+1] = min(a[i+1], a[i-1] + 2);
		if (i < N - 1) {
			b[i+1] = a[i+1]+1;
			if (firstfloor[i] + firstfloor[i+1] <= W)
				b[i+1] = min(b[i+1], c[i] + 1);
			
			c[i+1] = a[i+1]+1;
			if (secondfloor[i] + secondfloor[i+1] <= W)
				c[i+1] = min(c[i+1], b[i] + 1);
		}
	}
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
	int t;

	cin >> t;
	while (t--) {
		int result = 300000;
		cin >> N >> W;
		for (int i = 0; i < N; i++)
			cin >> firstfloor[i];
		for (int i = 0; i < N; i++)
			cin >> secondfloor[i];

		a[0] = 0;
		b[0] = 1;
		c[0] = 1;
		attack(0);
		result = min(result, a[N]);

		if (N > 1 && firstfloor[0] + firstfloor[N-1] <= W)
		{
			a[1] = 1;
			b[1] = 2;
			c[1] = 2;
			if (secondfloor[0] + secondfloor[1] <= W)
				c[1] = 1;
			attack(1);
			result = min(result, c[N-1] + 1);
		}
		if (N > 1 && secondfloor[0] + secondfloor[N-1] <= W) {
			a[1] = 1;
			c[1] = 2;
			b[1] = 2;
			if (firstfloor[0] + firstfloor[1] <= W)
				b[1] = 1;
			attack(1);
			result = min(result, b[N-1] + 1);
		}
		if (N > 1 && firstfloor[0] + firstfloor[N-1] <= W && secondfloor[0] + secondfloor[N-1] <= W) {
			a[1] = 0;
			b[1] = 1;
			c[1] = 1;
			attack(1);
			result = min(result, a[N-1] + 2);
		}
		cout << result << '\n';
	}
	return 0;
}