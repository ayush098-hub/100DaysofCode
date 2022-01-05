Question_Link: https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1/?category[]=Arrays&category[]=Arrays&company[]=Amazon&company[]=Amazon&problemStatus=solved&difficulty[]=0&difficulty[]=1&page=1&query=category[]Arrayscompany[]AmazonproblemStatussolveddifficulty[]0difficulty[]1page1company[]Amazoncategory[]Arrays

    
#User function Template for python3

class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        arr.sort()
        for i in range(len(arr)):
            if arr[i]==arr[k-1]:
                return arr[i]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    import random 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        ob=Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))
        
# } Driver Code Ends
