Question: https://practice.geeksforgeeks.org/problems/largest-element-in-array4009/1/?category[]=Arrays&category[]=Arrays&problemStatus=solved&page=1&query=category[]ArraysproblemStatussolvedpage1category[]Arrays
def largest( arr, n):
    
    max=0
    
    for i in range(n):
        if arr[i]>max:
         max=arr[i]
        
    return max

arr=[1, 8, 7, 56, 90]

print(largest(arr,len(arr)))
