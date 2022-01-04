Question_Link: https://practice.geeksforgeeks.org/problems/product-of-maximum-in-first-array-and-minimum-in-second3943/1/?category[]=Arrays&category[]=Arrays&problemStatus=unsolved&page=1&query=category[]ArraysproblemStatusunsolvedpage1category[]Arrays#
    
#User function Template for python3

class Solution:
    def find_multiplication (self, arr, brr, n, m) :
        max1=arr[0]
        min1=brr[0]
        
        for i in range(n):
            if arr[i]>max1:
                max1=arr[i]
                
        for j in range(m):
            if brr[j]<min1:
                min1=brr[j]
                
        return max1*min1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

    
    
for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    m = int(input())
    brr = list(map(int,input().strip().split()))
    ob=Solution()
    res = ob.find_multiplication(arr, brr, n, m)
    print(res)
