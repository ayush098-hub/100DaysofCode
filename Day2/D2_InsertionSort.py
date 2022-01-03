# Questionlink: https://www.codingninjas.com/codestudio/problems/insertion-sort_3155179

def insertionsort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        print("Key",key)

        j=i-1

        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
            
        arr[j+1]=key
        print(arr)

arr=[4,12,11,20]
insertionsort(arr)
print(arr)
