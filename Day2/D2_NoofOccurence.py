Quest: https://practice.geeksforgeeks.org/problems/number-of-occurrence2259/1/?category[]=Arrays&category[]=Arrays&problemStatus=unsolved&page=2&query=category[]ArraysproblemStatusunsolvedpage2category[]Arrays

#User function Template for python3
class Solution:
#Below is main code.
	def count(self,arr, n, x):
		
		ans=0
		
		for i in range(n):
		    if arr[i]==x:
		        ans=ans+1
		return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends
