#include<stdio.h>
#include<math.h>

int parent( int i) return (i-1)/2;

int left(int i) return 2*i+1;

int right(int i) return 2*i+2;

int swap(int *a, int *b)
{
	/**a = *a - *b;
	*b = *a + *b;
	*a = *b - *a;*/

	int temp;
	temp = *a;
	*a = *b;
	*b = temp;
}

/* Insert an element ele(int) to Max Heap*/
void insert( int *array, int n, int ele)
{
	int i=n+1;

	while( i!=0; array[i]> array[parent[i]]; i=parent(i))
	{
		swap( &array[i], &array[parent(i)]);
	}
	
}

void insert( int *array, int n, int ele)
{
	int i=n+1;

	while( i!=0; array[i]> array[parent[i]]; i=parent(i))
	{
		swap( &array[i], &array[parent(i)]);
	}
	
}

main()
{

	int array[]={1,3,5,4,6,13,10,9,8,15,17};
	int n = sizeof(array)/sizeof(array[0]);

	( array, n);
}