#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int N, M;
int waterpool[50][50];
int visited[50][50];
int dy[4] = {-1,1,0,0};
int dx[4] = {0,0,-1,1};


int bfs(int sy, int sx, int height)
{
	vector<pair<int, int>> queue = vector<pair<int, int>>();
	queue.push_back(pair<int, int>(sy,sx));
	visited[sy][sx] = 1;
	int flag = 1;
	int count = 1;
	while (!queue.empty())
	{
		pair<int, int> cur = queue.front();
		queue.erase(queue.begin());
		for (int i = 0; i < 4; i++)
		{
			int ny = dy[i] + cur.first;
			int nx = dx[i] + cur.second;

			if ((0 <= ny && ny < N) && (0 <= nx && nx < M))
			{
				if (visited[ny][nx] == 0 && waterpool[ny][nx] <= height)
				{
					visited[ny][nx] = 1;
					count++;
					queue.push_back(pair<int, int>(ny, nx));
				}
			}
			else
				flag = 0;
		}
	}
	if (flag == 0)
		return 0;
	return count;
}

int main(void)
{
	int result = 0;
	scanf("%d%d", &N, &M);
	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++)
			scanf("%1d", &waterpool[i][j]);
	for (int height = 1; height < 9; height++) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				visited[i][j] = 0;
			}
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (visited[i][j] == 0 && waterpool[i][j] <= height)
					result += bfs(i, j, height);
			}
		}
	}
	printf("%d", result);
	return 0;
}