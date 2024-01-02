#include <stdio.h>
#include <stdlib.h>
#define N 30

main()
{
	int sump=0,sumn=0,sum=0,i,pin[N];
	for(i=0;i<N;i++)
	{
		scanf("%d",&pin[i]);
		sum=sum+pin[i];
	}
	if(sum>100)
	{
		for(i=0;i<N;i++)
		{
			if(pin[i]>0)
				sump=sump+pin[i];
			else if(pin[i]<0)
				sumn=sumn+pin[i];
			else
				printf("%d",sum);
				break;	
		}
	}
	printf("%d %d",sump,sumn);
}
