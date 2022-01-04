Question lInk: https://practice.geeksforgeeks.org/problems/form-a-number-divisible-by-3-using-array-digits0717/1/?category[]=Arrays&category[]=Arrays&problemStatus=unsolved&difficulty[]=0&page=1&query=category[]ArraysproblemStatusunsolveddifficulty[]0page1category[]Arrays

#User function Template for python3

class Solution:
    def isPossible(self, N, arr):
        sum=0
        
        for i in range(N):
            sum=sum+arr[i]
        if sum%3==0:
            return 1
        else:
            return 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.isPossible(N, arr))
# } Driver Code Ends
