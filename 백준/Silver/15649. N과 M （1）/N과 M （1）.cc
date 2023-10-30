#include <cstdio>

int n,m;
int visited[10], path[10];

void f(int k)
{
	if(k>m)
	{
		for(int i=1;i<=m;i++)
		{
			printf("%d ",path[i]);
		}
		printf("\n");
		return;
	}
	for(int i=1;i<=n;i++)
	{
		if(visited[i]==0)
		{
			path[k]=i;
			visited[i]=1;
			f(k+1);
			visited[i]=0;
		}
	}
}

int main(){
	scanf("%d %d",&n,&m);
	f(1);
	return 0;
}