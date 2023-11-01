#include <iostream>
#include <vector>
using namespace std;
int N;
vector<vector<pair<int, int>>> graph = vector<vector<pair<int, int>>>();

pair<int, int> bfs(int start)
{
	int visited[N + 1] = {};
	int distance[N + 1] = {};
	int max_distance = 0;
	int max_node = start;
	visited[start] = 1;
	vector<int> queue = vector<int>();
	queue.push_back(start);
	while (!queue.empty())
	{
		int cur = queue.front();
		queue.erase(queue.begin());
		for (pair<int, int> nxt : graph[cur])
		{
			if (visited[nxt.first] == 0)
			{
				visited[nxt.first] = 1;
				distance[nxt.first] = distance[cur] + nxt.second;
				if (max_distance < distance[nxt.first])
				{
					max_distance = distance[nxt.first];
					max_node = nxt.first;
				}
				queue.push_back(nxt.first);
			}
		}
	}
	return pair(max_node, max_distance);
}

int main(void)
{
	cin >> N;
	for (int i = 0; i < N + 1; i++)
		graph.push_back(vector<pair<int, int>>());
	for (int i = 0; i < N - 1; i++)
	{
		int s, e, d;
		cin >> s >> e >> d;
		graph[s].push_back(pair(e, d));
		graph[e].push_back(pair(s, d));
	}
	pair<int, int> result;
	result = bfs(1);
	result = bfs(result.first);
	cout << result.second;
	return 0;
}