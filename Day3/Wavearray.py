Question_Link: https://practice.geeksforgeeks.org/problems/wave-array-1587115621/1/?category[]=Arrays&category[]=Arrays&problemStatus=unsolved&page=1&query=category[]ArraysproblemStatusunsolvedpage1category[]Arrays
    
def wave(arr):

    size=len(arr)
    for i in range(0,size,2):
         if i+1<size:
          if arr[i]<arr[i+1]:
           arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr
    

arr=[6907, 7808 ,8551, 8683, 9205, 9980]
print(wave(arr))
