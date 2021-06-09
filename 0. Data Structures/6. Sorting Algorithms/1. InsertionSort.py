# Insertion sort is proces of sorting an array.
# In insertian sort, we divide the array into two, sorted part and unsorted part.
# Every time we select the first element from the unsorted part and find its position in sorted part and insert there.
# At the beginning, we onsider the first element is sorted part and remaining part is unsorted part.

def insertionSort(list):
    for i in range(1,len(list)):
        value = list[i]
        j=i
        while( j>0 and list[j-1] > value ):
            list[j] = list[j-1]
            j=j-1
        list[j] = value
    return list

list = [50,20,80,10,60]
sorted = insertionSort(list)
print(sorted)