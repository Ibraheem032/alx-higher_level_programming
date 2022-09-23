#include <stdio.h>
#include <stdlib.h>
int main(int argc, char **argv)
{
	int i, result;
	unsigned int j;

	result = 0;
	for (i = 1; argv[i] != NULL; i++)
	{
		j = atoi(argv[i]);
		result = result + j;
	}
	printf("%i\n", result);
	return 0;
}
