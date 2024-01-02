#include <stdio.h>
#include <stdlib.h>

main()
{
	int i,j,w,st,x,y;
	scanf("%d%d%d",&st,&x,&y);
	for(w=0;w<st;w++)
		printf(" ");
	for(i=0;i<x;i++)
	{
		for(j=0;j<y;j++)	
			printf("\xDB");
	
		printf("\n");
		for(w=0;w<st;w++)
			printf(" ");
	}
}
