#include <bits/stdc++.h>
using namespace std;

int a[1030][1030], psum[1030][1030];
int N, M;
int e, f, g, h;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
	
	cin >> N >> M;
	for (int i = 1; i < N+1; i++) {
		for (int j = 1; j < N + 1; j++) {
			cin >> a[i][j];
			psum[i][j] = psum[i][j-1] + psum[i-1][j] - psum[i-1][j-1] + a[i][j];
		}
	}

	for (int i = 0; i < M; i++) {
		cin >> e >> f >> g >> h;
		cout << psum[g][h] - psum[g][f-1] - psum[e-1][h] + psum[e-1][f-1] << '\n';
	}
	return 0;
}