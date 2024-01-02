#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <string.h>

main()
{
	int i,j;
	for(i=1;i<=5;i++)
	{
		for(j=i;j<=9;j++)
			printf("%d",j);
		printf("\n");
	}
}
