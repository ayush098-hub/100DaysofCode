Question Link: https://www.codingninjas.com/codestudio/problems/bubble-sort_980524

def bubblesort(arr):
    n = len(arr)
    for i in range(0,n):
        swap =False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap=True
        if swap==False:
         break

    return arr

arr=[1,2,4,3,5]
print(bubblesort(arr))
