def bubbleSort(list):

    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list

list = [50,20,80,10,60]
sorted = bubbleSort(list)
print(sorted)