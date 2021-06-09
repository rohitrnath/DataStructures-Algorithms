# Selection sort is proces of sorting an array.
# In Selection sort, we take the smallest value in the array and  swap it with the first element in the unsorted part.

def selectionSort(list):
    for i in range(len(list)-1):
        minvalue = i
        for j in range(i+1,len(list)):
            if(list[minvalue] > list[j]):
                minvalue = j
        temp = list[i]
        list[i] = list[minvalue]
        list[minvalue] = temp
    return list

list = [50,20,80,10,60]
sorted = selectionSort(list)
print(sorted)
