Question Link: https://practice.geeksforgeeks.org/problems/sum-of-array2326/1/
    
    
#User function Template for python3
class Solution:

	def _sum(self,arr, n):
   		# code here
   		sum=0
   		for i in range(n):
   		    sum=sum+arr[i]
   		    
   		return sum
   		    


#{ 
#  Driver Code Starts
#Initial Template for Python 3




# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int , input().strip().split()))
        ob = Solution()
        ans = ob._sum(arr, n)
        print(ans)
        tc=tc-1
# } Driver Code Ends
