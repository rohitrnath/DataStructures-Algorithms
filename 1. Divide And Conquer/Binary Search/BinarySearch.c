#include <stdio.h>
/*
- Binary search can always done on sorted arrays.
- Mximum comparison required to seach for a number is the height of 
- the tree made using binarysearch algorithm.
- Height of a tree with n elements is log(n)
- So time coplexity is O[log(n)]
- Minimum time of binary search tree is O(1) and max is O[log(n)].
*/

int binarySearch( int *array, int count, int key)
{
	int low=0, mid, high=count-1;

	while(low <= high)
	{
		mid = (low+high)/2;

		if(array[mid] == key)
		{
			return mid;
		}
		else if(key < array[mid])
		{
			high = mid-11;
		}
		else
		{
			low = mid+1;
		}
	}
	return -1;
}


int main()
{
	int array[]= {10,20,30,40,50,60,70,80,90,100};

	int n = sizeof(array)/sizeof(array[0]);

	int key = 10; //the number need to search

	int result = binarySearch( array, n, key);

	printf( "pos : %d \n", result);
}