#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <string.h>

main()
{
	int i=0,x,y,pin[30];
	scanf("%d",&x);
	while(x/2!=0)
	{
		pin[i]=x%2;
		i++;
		x=x/2;
	}
	pin[i]=x%2;
	for(y=i;y>=0;y--)
		printf("%d",pin[y]);
}
