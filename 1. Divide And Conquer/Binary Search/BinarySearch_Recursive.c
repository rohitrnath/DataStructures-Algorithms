 #include <stdio.h>
/*
- Binary search can always done on sorted arrays.
- Mximum comparison required to seach for a number is the height of 
- the tree made using binarysearch algorithm.
- Height of a tree with n elements is log(n)
- So time coplexity is O[log(n)]
- Minimum time of binary search tree is O(1) and max is O[log(n)].
Recurrence Relation
	  { 1 for n =1
T(n) ={
	  {  T(n/2)+1    n>1

Applying master theorem, the time complexity is Theta[log(n)]
*/

int binarySearch_recr( int *array, int low, int high, int key)
{
	if( low == high) //single element only
	{
		if(array[low] == key)
		{
			return low;
		}
		else
		{
			return -1;
		}

	}
	else 
	{
		int mid = (low+high)/2;
		if(key == array[mid])
		{
			return mid;
		}
		else if( key < array[mid])
		{
			return binarySearch_recr( array, low, mid-1, key);
		}
		else
		{
			return binarySearch_recr( array, mid+1, high, key);
		}
	}
}


int main()
{
	int array[]= {10,20,30,40,50,60,70,80,90,100};

	int n = sizeof(array)/sizeof(array[0]);

	int key = 90; //the number need to search

	int result = binarySearch_recr( array, 0, n-1, key);

	printf( "pos : %d \n", result);

	return 0;
}