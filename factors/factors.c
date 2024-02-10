#include <stdio.h>
#include "factors.h"

void factorize(int n)
{
	printf("%d=", n);
	for (int i = 2; i <= n / 2; ++i)
	{
		if (n % i == 0)
		{
			printf("%d*%d\n", i, n / i);
			return;
		}
	}
	printf("%d*%d\n", 1, n);
}

int main(int argc, char *argv[])
{
	if (argc != 2)
	{
		printf("Usage: %s <file>\n", argv[0]);
		return (1);
	}

	FILE *file = fopen(argv[1], "r");
	if (file == NULL)
	{
		printf("Error opening file.\n");
		return (1);
	}
	int num;
	while (fscanf(file, "%d", &num) == 1)
	{
		factorize(num);
	}

	fclose(file);

	return (0);
}
