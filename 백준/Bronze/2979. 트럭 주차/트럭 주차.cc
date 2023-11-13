#include <bits/stdc++.h>
using namespace std;

int arr[104];
int A, B, C, a ,b, ret;
int main() {
	cin >> A >> B >> C;
	for (int i = 0; i < 3; i++) {
		cin >> a >> b;
		for (int j = a; j < b; j++) arr[j]++;
	}
	for (int i = 1; i < 100; i++) {
		if (arr[i]) {
			if (arr[i] == 1) ret += A;
			else if (arr[i] == 2) ret += B * 2;
			else if (arr[i] == 3) ret += C * 3;
		}
	}
	cout << ret << '\n';
	return 0;
}