#include<ios>

int t,m,n,k,i,j,c,q,w,a[51][51];
void d(int x,int y)
{
	if (a[x][y]==1)
	{
		a[x][y]=0;
		d(x-1,y);
		d(x+1,y);
		d(x,y-1);
		d(x,y+1);
	}		
}

int main()
{
	scanf("%d",&t);
	while (t--)
	{
		c=0;
		scanf("%d%d%d",&m,&n,&k);
		for ( i = 0; i < k; i++)
		{
			scanf("%d%d",&q,&w);
			a[q][w]=1;
		}
		for (i = 0; i < m; i++)
			for(j = 0; j < n; j++)
				if(a[i][j] == 1)
				{
					c++;
					d(i,j);
				}
		printf("%d ",c);
	}
}