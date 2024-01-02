#include <stdio.h>
#include <stdlib.h>

main()
{
	int i,j;
	for(i=0;i<20;i++)
	{
		for(j=0;j<40;j++)
			printf("\xDB");
		printf("\n");
	}
}
