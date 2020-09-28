def insertionSort(list):
    for i in range (0,len(list)):
        key= list[i]
        j=i-1
        while(j>=0 and key<list[j]):
            list[j+1] = list[j]
            j-=1
        list[j+1]=key
    return list

arr=[12,11,135,6,88,64, 2 , 452 , 764, 54 ,654, 9876 ,96,4343,676,3241,0 ,85646, 235]
print(insertionSort(arr))



